from app import db

class Agenda(db.Model):
    __tablename__ = 'agendas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(500))

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "data": str(self.data),
            "descricao": self.descricao
        }
