import dotenv
from flask import Flask, render_template, redirect, url_for, request
import logging
import os
from models.model import *

path = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(path, 'static')
template_folder = os.path.join(path, 'templates')
log_folder = os.path.join(path, 'log')

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder,)

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename=f"{log_folder}/app.log", level=logging.DEBUG, format=log_format)

usuarios = Lista_Usuarios()
usuarios.adicionar_usuario("Schopenhauer", "moto", "sim")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/trust")
def trust_in_me():
    return render_template("trust_in_me.html")

@app.route("/manual")
def manual():
    return render_template("user_manual.html")

@app.route("/create_user", methods=["GET","POST"])
def create_user():
    if request.method == "POST":
        nome = request.form["nome"]
        veiculo = request.form["tipo_veiculo"]
        cnh = request.form["cnh"]
        novo_usuario = Criar_usuario(nome, veiculo, cnh)
        usuarios.adicionar_usuario(novo_usuario)
    return render_template("manage_users.html")


@app.route("/routes")
def route_management():

    atual = usuarios.cabeca
    while atual is not None:
        nome = atual.nome
        veiculo = atual.veiculo
        cnh = atual.cnh
        atual = atual.proximo
    return render_template("route_management.html", nome=nome, veiculo=veiculo, cnh=cnh)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)