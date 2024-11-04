from app import db
from datetime import datetime

class Cirurgia(db.Model):
    __tablename__ = 'cirurgia'
    id_cirurgia = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(128), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))

    def __init__(self, tipo, data, descricao, paciente_id):
        self.tipo = tipo
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.descricao = descricao
        self.paciente_id = paciente_id

    def to_dict(self):
        return {
            'id_cirurgia': self.id_cirurgia,
            'tipo': self.tipo,
            'data': self.data.strftime('%Y-%m-%d'),
            'descricao': self.descricao,
            'paciente_id': self.paciente_id,
        }
