from app import db
from datetime import datetime

class Financeiro(db.Model):
    __tablename__ = 'financeiro'
    id_financeiro = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    valor = db.Column(db.Float, nullable=False)
    data_transacao = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Tipo de transação (receita, despesa)

    def __init__(self, descricao, valor, data_transacao, tipo):
        self.descricao = descricao
        self.valor = valor
        self.data_transacao = datetime.strptime(data_transacao, '%Y-%m-%d')
        self.tipo = tipo

    def to_dict(self):
        return {
            'id_financeiro': self.id_financeiro,
            'descricao': self.descricao,
            'valor': self.valor,
            'data_transacao': self.data_transacao.strftime('%Y-%m-%d'),
            'tipo': self.tipo,
        }
