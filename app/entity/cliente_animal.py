from app import db
from datetime import datetime

class ClienteAnimal(db.Model):
    __tablename__ = 'cliente_animal'
    id_cliente_animal = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    especie = db.Column(db.String(128), nullable=False)
    raca = db.Column(db.String(128))
    idade = db.Column(db.Integer)
    cliente_pessoa_id = db.Column(db.Integer, db.ForeignKey('cliente_pessoa.id_cliente_pessoa'))

    def __init__(self, nome, especie, raca, idade, cliente_pessoa_id):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.cliente_pessoa_id = cliente_pessoa_id

    def to_dict(self):
        return {
            'id_cliente_animal': self.id_cliente_animal,
            'nome': self.nome,
            'especie': self.especie,
            'raca': self.raca,
            'idade': self.idade,
            'cliente_pessoa_id': self.cliente_pessoa_id,
        }
