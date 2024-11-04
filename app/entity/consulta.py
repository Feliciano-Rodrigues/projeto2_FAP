from app import db
from datetime import datetime

class Consulta(db.Model):
    __tablename__ = 'consulta'
    id_consulta = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinario.id_veterinario'))
    cliente_animal_id = db.Column(db.Integer, db.ForeignKey('cliente_animal.id_cliente_animal'))

    def __init__(self, data, descricao, veterinario_id, cliente_animal_id):
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.descricao = descricao
        self.veterinario_id = veterinario_id
        self.cliente_animal_id = cliente_animal_id

    def to_dict(self):
        return {
            'id_consulta': self.id_consulta,
            'data': self.data.strftime('%Y-%m-%d'),
            'descricao': self.descricao,
            'veterinario_id': self.veterinario_id,
            'cliente_animal_id': self.cliente_animal_id,
        }
