from app import db
from datetime import datetime

class Prescricao(db.Model):
    __tablename__ = 'prescricao'
    id_prescricao = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    data = db.Column(db.Date, nullable=False)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'))

    def __init__(self, descricao, data, consulta_id):
        self.descricao = descricao
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.consulta_id = consulta_id

    def to_dict(self):
        return {
            'id_prescricao': self.id_prescricao,
            'descricao': self.descricao,
            'data': self.data.strftime('%Y-%m-%d'),
            'consulta_id': self.consulta_id,
        }
