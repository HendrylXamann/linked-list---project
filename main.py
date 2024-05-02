from flask import Flask, render_template, redirect, url_for, request
import logging
import os
from models.model import *
from operator import attrgetter

path = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(path, 'static')
template_folder = os.path.join(path, 'templates')
log_folder = os.path.join(path, 'log')

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder,)

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename=f"{log_folder}/app.log", level=logging.DEBUG, format=log_format)

#Instanciando a classe p/ definir um valor default
usu = Lista_Usuarios()
usu.adicionar_usuario("Schopenhauer", "moto", "sim")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/manual")
def manual():
    return render_template("user_manual.html")

@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        nome = request.form["nome"]
        veiculo = request.form["tipo_veiculo"]
        cnh = request.form["cnh"]
        usu.adicionar_usuario(nome, veiculo, cnh)
        return render_template("manage_users.html", message=f'Usuario {nome} criado com sucesso!')
    return render_template("manage_users.html")

@app.route("/routes", methods=["GET", "POST"])
def route_management():
    usuarios = usu.listar_usuarios()
    rotasList = ListaRotas()
    rotas = rotasList.rotas
    rotas_ordenadas = sorted(rotas, key=attrgetter('prioridade'))
    rotas_obj = Rotas()
    id = rotas_obj.id
    prioridade = rotas_obj.prioridade
    if request.method == "POST":
        prioridade = int(request.form.get("prioridade"))
        funcionario = request.form.get("funcionario")
        id_rota = int(request.form.get("id_rota"))
        for rota in rotasList.rotas:
            if id_rota == rotas_obj.id:
                rota.alterar_prioridade(prioridade)
                rota.alterar_funcionario(funcionario)

    return render_template("route_management.html", rotas=rotas_ordenadas, funcionarios=usuarios, id=id, prioridade=prioridade)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

# Falta 2 coisas:
# 1. Finalizar o endpoint routes
# 2. Ajustar as classes para lista encadeada;