from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email, cpf, telefone)
        VALUES (?, ?, ?, ?)
    """, (nome, email, cpf, telefone))

    conn.commit()
    conn.close()

    return redirect("/")
if __name__ == "__main__":
    app.run()
