from app import db
from ..entity.consulta import Consulta

class ConsultaRepository:
    def add(self, consulta):
        db.session.add(consulta)
        db.session.commit()

    def get_all(self):
        return Consulta.query.all()

    def get_by_id(self, id):
        return Consulta.query.get(id)

    def update(self, consulta):
        db.session.merge(consulta)
        db.session.commit()

    def delete(self, consulta):
        db.session.delete(consulta)
        db.session.commit()
