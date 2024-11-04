from app import db
from ..entity.exame import Exame

class ExameRepository:
    def add(self, exame):
        db.session.add(exame)
        db.session.commit()

    def get_all(self):
        return Exame.query.all()

    def get_by_id(self, id):
        return Exame.query.get(id)

    def update(self, exame):
        db.session.merge(exame)
        db.session.commit()

    def delete(self, exame):
        db.session.delete(exame)
        db.session.commit()
