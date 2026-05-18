import random
import string
import sqlite3

Token = ""


def gerador():
    while True:
        print("Bem-Vindo Ao Gerador De Tokens")
        Alternativa = input("Você quer gerar uma Token: ".lower())
        Caracteres = int(input("Quantos Caracteres deseja:  "))
        especial = input("Você Deseja Caracteres Especiais:  ".lower())

        if Alternativa == "sim" and especial == "sim" and Caracteres > 0:
            Token = ""
            for _ in range(Caracteres):
                caracter = string.ascii_letters + string.digits + string.punctuation
                Token += random.choice(caracter)
            return Token
        elif Alternativa == "sim" and Caracteres > 0:
            Token = ""
            for _ in range(Caracteres):
                caracter = string.ascii_letters + string.digits
                Token += random.choice(caracter)
            return Token
        else:
            print("Não foi Gerada A Sua Token")
        while True:
            opcao = input("Deseja reiniciar (S/N)? ").lower()
            if opcao not in ("s", "n"):
                print("opcao invalida, deve ser S ou N")
            elif opcao == "n":
                break
            else:
                break


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
        (Token, forca),
    )
    connect.commit()

    cursor.execute("SELECT * FROM Tokens")
    print(cursor.fetchall())

    connect.close()


Salvar()
