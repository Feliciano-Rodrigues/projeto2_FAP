from app import db
from app.entity.agenda import Agenda

class AgendaRepository:
    def add(self, agenda):
        db.session.add(agenda)
        db.session.commit()

    def get_all(self):
        return Agenda.query.all()

    def get_by_id(self, id):
        return Agenda.query.get(id)

    def update(self, agenda):
        db.session.merge(agenda)
        db.session.commit()

    def delete(self, agenda):
        db.session.delete(agenda)
        db.session.commit()
