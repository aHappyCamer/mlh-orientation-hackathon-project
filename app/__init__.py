import os
from flask import Flask, render_template
from . import db

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

import os
from flask import Flask, request, render_template

app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')

import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))

@app.route('/health')
def check():
    return 'Works'
