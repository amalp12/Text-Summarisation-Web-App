    
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
"""

############### Model Start #####################
import torch
from transformers import pipeline

summarizer = pipeline("summarization")

def model_forward(article): 
    summary = '' 
    for i in range (int(len(article)/1024)):
        summary+=summarizer(article[1024*(i-1):1024*i], max_length=100, min_length=50, do_sample=False)[0]
        #print(summary['summary_text'])
    return summary
    

############### Model End #################
"""

@app.route('/landing' )#, methods = ['GET','POST' ])
def landing():

    return render_template("landing.html")



@app.route('/' , methods = ['GET','POST' ])
def index():

    return render_template("index.html")


@app.route("/submit/", methods = ["POST"])
def submit_text():
    if request.method == 'POST':
        
        text = request.form['submit-textbox']
        summary = model_forward(text)
        print(summary)
        
        return render_template("landing.html" ,  summary = summary)


if __name__ == 'main':
    app.run(debug=True)