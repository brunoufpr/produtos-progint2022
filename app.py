import json
from flask import Flask, redirect, render_template, request, url_for
import psycopg2
import psycopg2.extras
from model import Produto, db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bruno123@localhost:5432/produtos'
db.init_app(app)
migrate= Migrate(app,db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def produtos ():
    #Carregar filial
    id_f = 1  ## TODO: apos fazer o login, substituir pelo usuario logado

    #Carregar os produtos do Banco
    produtos = Produto.query.filter_by(id_filial=id_f).all()  # lista de produtos. Ex: [p1,p2,p3]

    #Renderizar o template (pagina) passando a lista de produtos
    return render_template("produtos.html",prods=produtos)


@app.route('/cadastrar_produto_form')
def cadastrar_produto_form ():
    return render_template("cadastrar_produto.html")


@app.post('/cadastrar_produto_action')
def cadastrar_produto_action():

    nom = request.form['nome']
    preco= request.form['preco']
    qtd_estoque = request.form ['qtd_estoque']
    descricao= request.form ['descricao']
    id_filial = 1   # TODO: apos fazer o login, substituir pelo id do usuario logado

    prod = Produto(nome=nom, preco=preco, qtd_estoque=qtd_estoque, descricao=descricao, id_filial=id_filial)
    db.session.add(prod)
    db.session.commit()

    return redirect(url_for("produtos"))