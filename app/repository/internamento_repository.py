from app import db
from ..entity.internamento import Internamento

class InternamentoRepository:
    def add(self, internamento):
        db.session.add(internamento)
        db.session.commit()

    def get_all(self):
        return Internamento.query.all()

    def get_by_id(self, id):
        return Internamento.query.get(id)

    def update(self, internamento):
        db.session.merge(internamento)
        db.session.commit()

    def delete(self, internamento):
        db.session.delete(internamento)
        db.session.commit()
