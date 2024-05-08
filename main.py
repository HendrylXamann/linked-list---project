from flask import Flask, render_template, request
import os
import logging
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

#Instanciando as classes p/ definir os valores default (usando list comprehension p enbelezar o código) :)
usu = Lista_Usuarios()
usuarios = [("Kant", "moto", "sim"), ("Nietzsche", "moto", "sim"), ("Schopenhauer", "moto", "sim"), ("Hegel", "moto", "sim")]
[usu.adicionar_usuario(*usuario) for usuario in usuarios]

rotasList = ListaRotas()
rotas = [(1, 3, "Kant"), (2, 2, "Nietzsche"), (3, 1, "Schopenhauer"), (4, 3, "Hegel")]
[rotasList.adicionar_rota(Rotas(id=id, prioridade=prioridade, funcionario=funcionario)) for id, prioridade, funcionario in rotas]

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
