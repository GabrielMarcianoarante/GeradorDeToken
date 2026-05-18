from flask import Flask, jsonify, request, sqlite3

app = Flask(__name__)


@app.route("/tokens", methods=["GET"])
def get_tokens():
    connect = sqlite3.connect("Token.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Tokens")
    tokens = cursor.fetchall()
    connect.close()
    return jsonify(tokens)
