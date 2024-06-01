from flask import Flask, render_template, request
import os
import logging
from models.modeltp1 import *
from models.modeltp2 import *

def carregando_envs():
    path = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(path, 'static')
    template_folder = os.path.join(path, 'templates')
    log_folder = os.path.join(path, 'log')
    return static_folder, template_folder, log_folder

def config_log():
    log_folder = carregando_envs()[2]
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        filename=f"{log_folder}/app.log", level=logging.DEBUG, format=log_format)
    
app = Flask(__name__, template_folder=carregando_envs()[1],
            static_folder=carregando_envs()[0],)

config_log()

def atributos_basicos() -> tuple:
    #Instanciando as classes p/ definir os valores default (usando list comprehension p enbelezar o código) :)
    usu = Lista_Usuarios()
    usuarios = [("Kant", "moto", "sim"), ("Nietzsche", "moto", "sim"), ("Schopenhauer", "moto", "sim"), ("Hegel", "moto", "sim")]
    [usu.adicionar_usuario(*usuario) for usuario in usuarios]

    rotas = [(1, 3, "Kant"), (2, 2, "Nietzsche"), (3, 1, "Schopenhauer"), (4, 3, "Hegel")]
    arvore_rotas = ArvoreBiBusca()
    [arvore_rotas.inserir(id, funcionario, prioridade) for id, prioridade, funcionario in rotas]

    return usu, arvore_rotas
    
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/manual")
def manual():
    return render_template("user_manual.html")

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
    usu, arvore_rotas= atributos_basicos()
    usuarios = usu.listar_usuarios()
    tdas_rotas = arvore_rotas.listar_rotas()
    if request.method == "POST":
        rotas_para_excluir = []

        for rota in tdas_rotas:
            rota_id = rota[0]
            print(f"Processando rota {rota_id}")

            if request.form.get("excluir_" + str(rota_id)):
                rotas_para_excluir.append(rota_id)
                continue

            novo_funcionario = request.form.get("funcionario_" + str(rota_id))
            nova_prioridade = request.form.get("prioridade_" + str(rota_id))
            if novo_funcionario and nova_prioridade:
                nova_prioridade = int(nova_prioridade)
                # Atualiza a prioridade apenas se for diferente
                if rota[2] != nova_prioridade:
                    arvore_rotas.alterar_prioridade(rota_id, nova_prioridade)
                    pass

                # Atualiza o funcionário apenas se for diferente
                if rota[1] != novo_funcionario:
                    novo_usuario = next((usuario for usuario in usuarios if usuario.nome == novo_funcionario), None)
                    if novo_usuario:
                        arvore_rotas.alterar_funcionario(rota_id, novo_usuario.nome)
                    pass

        for rota_id in rotas_para_excluir:
            print(f"Excluindo rota {rota_id}")
            arvore_rotas.delete(rota_id)

        tdas_rotas = arvore_rotas.listar_rotas()
        return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios, message='Alteração realizada!')

    return render_template("route_management.html", rotas=tdas_rotas, funcionarios=usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

