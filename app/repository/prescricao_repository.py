from app import db
from ..entity.prescricao import Prescricao

class PrescricaoRepository:
    def add(self, prescricao):
        db.session.add(prescricao)
        db.session.commit()

    def get_all(self):
        return Prescricao.query.all()

    def get_by_id(self, id):
        return Prescricao.query.get(id)

    def update(self, prescricao):
        db.session.merge(prescricao)
        db.session.commit()

    def delete(self, prescricao):
        db.session.delete(prescricao)
        db.session.commit()
