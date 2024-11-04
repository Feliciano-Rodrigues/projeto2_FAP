from app import db
from datetime import datetime

class Medicamento(db.Model):
    __tablename__ = 'medicamento'
    id_medicamento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(255))
    fabricante = db.Column(db.String(128))
    data_validade = db.Column(db.Date, nullable=False)
    prescricao_id = db.Column(db.Integer, db.ForeignKey('prescricao.id_prescricao'))

    def __init__(self, nome, descricao, fabricante, data_validade, prescricao_id):
        self.nome = nome
        self.descricao = descricao
        self.fabricante = fabricante
        self.data_validade = datetime.strptime(data_validade, '%Y-%m-%d')
        self.prescricao_id = prescricao_id

    def to_dict(self):
        return {
            'id_medicamento': self.id_medicamento,
            'nome': self.nome,
            'descricao': self.descricao,
            'fabricante': self.fabricante,
            'data_validade': self.data_validade.strftime('%Y-%m-%d'),
            'prescricao_id': self.prescricao_id,
        }
