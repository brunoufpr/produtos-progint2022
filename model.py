from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



    
class Filial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)



class Produto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String,nullable=False)
    preco= db.Column(db.Numeric,nullable=False)
    qtd_estoque= db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String,)
    id_filial= db.Column(db.Integer,db.ForeignKey(Filial.id))
