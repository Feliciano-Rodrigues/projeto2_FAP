from app import db

class Exame(db.Model):
    __tablename__ = 'exame'
    id_exame = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(128), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'))

    def __init__(self, tipo, data, descricao, consulta_id):
        self.tipo = tipo
        self.data = data
        self.descricao = descricao
        self.consulta_id = consulta_id

    def to_dict(self):
        return {
            'id_exame': self.id_exame,
            'tipo': self.tipo,
            'data': self.data.strftime('%Y-%m-%d'),
            'descricao': self.descricao,
            'consulta_id': self.consulta_id
        }
