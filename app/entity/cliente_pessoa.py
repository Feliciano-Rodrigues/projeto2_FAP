from app import db
from datetime import datetime

class ClientePessoa(db.Model):
    __tablename__ = 'cliente_pessoa'
    id_cliente_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    endereco = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, CPF, telefone, email, endereco, data_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')

    def to_dict(self):
        return {
            'id_cliente_pessoa': self.id_cliente_pessoa,
            'nome': self.nome,
            'CPF': self.CPF,
            'telefone': self.telefone,
            'email': self.email,
            'endereco': self.endereco,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
        }
