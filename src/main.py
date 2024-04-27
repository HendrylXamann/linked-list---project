import io
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime, timedelta
from config import Config
import os
from models.model import *

static_folder = os.environ.get("STATIC_FD") 
template_folder = os.environ.get("TEMPLATE_FD") 

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder,)
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/trust_in_me")
def trust_in_me():
    return render_template("trust_in_me.html")

@app.route("/user_manual")
def manual():
    return render_template("user_manual.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    # Obter dados do formulário
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    # Criar novo usuário
    create_user(name, email, password)

    # Redirecionar para a página de gerenciamento de usuários
    return redirect(url_for("manage_users"))

@app.route("/manage_users")
def manage_users():
    users = get_all_users()
    return render_template("manage_users.html", users=users)

@app.route("/route_management")
def route_management():
    routes = get_all_routes()
    return render_template("route_management.html", routes=routes)


