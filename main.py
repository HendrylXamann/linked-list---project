from flask import Flask, render_template, request
import os
import logging
from models.modeltp1 import *
from models.modeltp2 import *

path = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(path, 'static')
template_folder = os.path.join(path, 'templates')
log_folder = os.path.join(path, 'log')

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder,)

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename=f"{log_folder}/app.log", level=logging.DEBUG, format=log_format)

#Instanciando as classes p/ definir os valores default (usando list comprehension p enbelezar o código) :)
usu = Lista_Usuarios()
usuarios = [("Kant", "moto", "sim"), ("Nietzsche", "moto", "sim"), ("Schopenhauer", "moto", "sim"), ("Hegel", "moto", "sim")]
[usu.adicionar_usuario(*usuario) for usuario in usuarios]

rotas = [(1, 3, "Kant"), (2, 2, "Nietzsche"), (3, 1, "Schopenhauer"), (4, 3, "Hegel")]
arvore_rotas = ArvoreBiBusca()
[arvore_rotas.inserir(id, funcionario, prioridade) for id, prioridade, funcionario in rotas]
rotasList = arvore_rotas.listar_rotas()


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/manual")
def manual():
    return render_template("user_manual.html")

@app.route("/routesTP1", methods=["GET", "POST"])
def route_managementTp1():
    usuarios = usu.listar_usuarios()
    tdas_rotas = rotasList.listar_rotas()
    if request.method == "POST":
        for rota in tdas_rotas:
            rota_id = rota.id
            novo_funcionario = request.form["funcionario_" + str(rota_id)]
            nova_prioridade = int(request.form["prioridade_" + str(rota_id)])
            rota.alterar_prioridade(nova_prioridade)
            
            novo_usuario = None
            for usuario in usuarios:
                if usuario.nome == novo_funcionario:
                    novo_usuario = usuario
                    break
            if novo_usuario: #mds era só isso  
                rota.alterar_funcionario(novo_usuario)

            if request.form.get("excluir_" + str(rota_id)):
                rotasList.remover_rota(rota_id)

        tdas_rotas = rotasList.listar_rotas()
        return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios, message=f'Alteração realizada!')

    return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios)

@app.route("/create_route", methods=["GET", "POST"])
def create_route():
    new_rotas = ArvoreBiBusca()
    if request.method == "POST":
        n_rota = request.form["rota_id"]
        funcionario = request.form["funcionario_rota"]
        prioridade = request.form["prioridade_rota"]
        new_rotas.inserir(n_rota, funcionario,prioridade)
        return render_template("create_route.html", message='Rota criada com sucesso!')
    return render_template("create_route.html")

@app.route("/routes", methods=["GET", "POST"])
def route_managementTp2():
    usuarios = usu.listar_usuarios()
    tdas_rotas = arvore_rotas.listar_rotas()
    if request.method == "POST":
        for rota in tdas_rotas:
            rota_id = rota[0]  # rota é uma tupla (id, funcionario, prioridade)
            novo_funcionario = request.form["funcionario_" + str(rota_id)]
            nova_prioridade = int(request.form["prioridade_" + str(rota_id)])
            arvore_rotas.alterar_prioridade(rota_id, nova_prioridade)
            
            novo_usuario = next((usuario for usuario in usuarios if usuario.nome == novo_funcionario), None)
            if novo_usuario:
                arvore_rotas.alterar_funcionario(rota_id, novo_usuario)

            if request.form.get("excluir_" + str(rota_id)):
                arvore_rotas.delete(rota_id)

        tdas_rotas = arvore_rotas.listar_rotas()
        return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios, message='Alteração realizada!')

    return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
