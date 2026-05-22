from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import sqlite3
import routes.gerador as gerador

app = Flask(__name__)

# Libera acesso do frontend
CORS(app)

@app.route("/tokens", methods=["GET"])
def get_tokens():

    try:
        # conecta no banco
        connect = sqlite3.connect("Token.db")

        # permite acessar colunas pelo nome
        connect.row_factory = sqlite3.Row

        cursor = connect.cursor()

        # busca tokens
        cursor.execute("SELECT * FROM Tokens")

        tokens = cursor.fetchall()

        # transforma em lista de dicionários
        resultado = [dict(token) for token in tokens]

        connect.close()

        return jsonify(resultado)

    except Exception as erro:

        return jsonify({
            "erro": str(erro)
        }), 500

@app.route("/gerar-token", methods=["POST"])
def gerar_token():
    try:
        gerador.Salvar()
        return jsonify({
            "mensagem": "Token gerado e salvo com sucesso!"
        })
    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500

@app.route("/")
def index():
    return "Bem-vindo ao Gerador de Tokens!"

@app.route("/receber-valor", methods=["POST", "GET"])
def recebertoken():
    if request.method == "POST":
        data = request.get_json()
        token = data.get("token")
        print(f"Token recebido: {token}")
        return jsonify({"mensagem": "Token recebido com sucesso!"})
    else:
        return jsonify({"mensagem": "Envie um token usando POST."})

@app.route("/quantidade", methods=["POST"])
def receber_quantidade():
    data = request.get_json()
    quantidade = data.get("quantidade")
    print(f"Quantidade recebida: {quantidade}")
    return jsonify({"mensagem": "Quantidade recebida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)