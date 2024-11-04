from app import db
from datetime import datetime

class Veterinario(db.Model):
    __tablename__ = 'veterinario'
    id_veterinario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    CRMV = db.Column(db.String(15), nullable=False, unique=True)
    especialidade = db.Column(db.String(128), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, CPF, CRMV, especialidade, telefone, email, data_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.CRMV = CRMV
        self.especialidade = especialidade
        self.telefone = telefone
        self.email = email
        self.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')

    def to_dict(self):
        return {
            'id_veterinario': self.id_veterinario,
            'nome': self.nome,
            'CPF': self.CPF,
            'CRMV': self.CRMV,
            'especialidade': self.especialidade,
            'telefone': self.telefone,
            'email': self.email,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
        }
