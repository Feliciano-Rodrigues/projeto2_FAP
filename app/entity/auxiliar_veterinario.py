from app import db
from datetime import datetime

class AuxiliarVeterinario(db.Model):
    __tablename__ = 'auxiliar_veterinario'
    id_auxiliar_veterinario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    especialidade = db.Column(db.String(128), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, CPF, especialidade, telefone, email, data_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.especialidade = especialidade
        self.telefone = telefone
        self.email = email
        self.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')

    def to_dict(self):
        return {
            'id_auxiliar_veterinario': self.id_auxiliar_veterinario,
            'nome': self.nome,
            'CPF': self.CPF,
            'especialidade': self.especialidade,
            'telefone': self.telefone,
            'email': self.email,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
        }
