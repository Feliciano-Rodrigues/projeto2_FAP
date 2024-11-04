from app import db
from datetime import datetime
import bcrypt

class Administradores(db.Model):
    __tablename__ = 'administradores'
    id_administrador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    login = db.Column(db.String(128), nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, CPF, telefone, email, login, senha):
        self.nome = nome
        self.CPF = CPF
        self.telefone = telefone
        self.email = email
        self.login = login
        self.set_senha(senha)

    def set_senha(self, senha):
        self.senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    def check_senha(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha_hash)

    def to_dict(self):
        return {
            'id_administrador': self.id_administrador,
            'nome': self.nome,
            'CPF': self.CPF,
            'telefone': self.telefone,
            'email': self.email,
            'login': self.login,
        }
