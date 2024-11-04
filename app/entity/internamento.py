from app import db
from datetime import datetime

class Internamento(db.Model):
    __tablename__ = 'internamento'
    id_internamento = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date)
    descricao = db.Column(db.String(255))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))

    def __init__(self, data_entrada, data_saida, descricao, paciente_id):
        self.data_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
        self.data_saida = datetime.strptime(data_saida, '%Y-%m-%d') if data_saida else None
        self.descricao = descricao
        self.paciente_id = paciente_id

    def to_dict(self):
        return {
            'id_internamento': self.id_internamento,
            'data_entrada': self.data_entrada.strftime('%Y-%m-%d'),
            'data_saida': self.data_saida.strftime('%Y-%m-%d') if self.data_saida else None,
            'descricao': self.descricao,
            'paciente_id': self.paciente_id,
        }
