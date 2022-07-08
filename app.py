import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def produtos ():
    json_file = open('dados/produtos.json',"r") 
    produtosjson = json.load(json_file)
    return render_template("produtos.html", produtos=produtosjson['produtos'])

