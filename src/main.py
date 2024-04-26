import io
from flask import Flask, render_template, redirect, url_for, request, make_response, send_file
from datetime import datetime, timedelta
from config import Config
import os
from models.model import *

static_folder = os.environ.get("STATIC_FOLDER") 
template_folder = os.environ.get("TEMPLATE_FOLDER") 

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder,)
app.config.from_object(Config)
init_app(app)


