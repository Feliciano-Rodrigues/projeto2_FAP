from app import db
from ..entity.cirurgia import Cirurgia

class CirurgiaRepository:
    def add(self, cirurgia):
        db.session.add(cirurgia)
        db.session.commit()

    def get_all(self):
        return Cirurgia.query.all()

    def get_by_id(self, id):
        return Cirurgia.query.get(id)

    def update(self, cirurgia):
        db.session.merge(cirurgia)
        db.session.commit()

    def delete(self, cirurgia):
        db.session.delete(cirurgia)
        db.session.commit()
