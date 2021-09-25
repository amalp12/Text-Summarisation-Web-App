    
from typing import Text
from flask import Flask, render_template, request, redirect
import flask
from model.TEXT_SUMMARIZATION_BERT import model_forward
#from requests import request

import requests

# Bash
# export FLASK_APP=application.py
# flask run
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)

#SERVER_URL = 'http://127.0.0.1:5000/'


        

@app.route('/' , methods = ['GET','POST' ])
def index():

    return render_template("index.html")


@app.route("/", methods = ["POST"])
def search():
    if request.method == 'POST':
        
        text = request.form['search-textbox']
        summary = model_forward(text)
        
        return redirect(flask.url_for('search_page',  summary = summary))



if __name__ == 'main':
    app.run(debug=True)