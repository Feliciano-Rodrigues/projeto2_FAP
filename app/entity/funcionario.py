from app import db
from datetime import datetime
import bcrypt

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id_funcionario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(255))
    data_nascimento = db.Column(db.Date, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, CPF, email, telefone, endereco, data_nascimento, senha):
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
        self.set_senha(senha)

    def set_senha(self, senha):
        self.senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    def check_senha(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha_hash)

    def to_dict(self):
        return {
            'id_funcionario': self.id_funcionario,
            'nome': self.nome,
            'CPF': self.CPF,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
        }
