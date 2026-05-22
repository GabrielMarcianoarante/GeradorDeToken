import random
import string
import sqlite3
import requests
Token = ""
quantidade = 0
Caracteres = 0

def receberquantidade():
    global quantidade
    global Caracteres
    Caracteres = requests.get("http://127.0.0.1:5000/receber-valor").json().get("caracteres", 0)
    quantidade = requests.get("http://127.0.0.1:5000/receber-valor").json().get("quantidade", 0)
def gerador():
    if quantidade < 1 or Caracteres < 1:
        while True:
                Token = ""
                for _ in range(Caracteres):
                    caracter = string.ascii_letters + string.digits + string.punctuation
                    Token += random.choice(caracter)
                return Token

def gerador_com_especial():
    while True:
        Token = ""
        for _ in range(Caracteres):
            caracter = string.ascii_letters + string.digits + string.punctuation
            Token += random.choice(caracter)
        if any(c in string.punctuation for c in Token):
            return Token
        print("Não foi Gerada A Sua Token")

def Verificar(Token):
    leitor = len(Token)
    if leitor <= 6:
        return "Token fraca"
    elif leitor <= 12:
        return "Token Média"
    else:
        return "Token Forte"


def Salvar():

    Token = gerador()

    forca = Verificar(Token)

    connect = sqlite3.connect("Token.db")

    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Token TEXT NOT NULL,
            forca TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT INTO Tokens (Token, forca) VALUES (?, ?)",
        (Token, forca)
    )

    connect.commit()

    connect.close()

    print("Token salva com sucesso!")

def Tokens_gerador():
    for _ in range(quantidade):
        gerador()
        Salvar()

Tokens_gerador()