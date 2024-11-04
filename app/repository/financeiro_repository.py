from app import db
from ..entity.financeiro import Financeiro

class FinanceiroRepository:
    def add(self, financeiro):
        db.session.add(financeiro)
        db.session.commit()

    def get_all(self):
        return Financeiro.query.all()

    def get_by_id(self, id):
        return Financeiro.query.get(id)

    def update(self, financeiro):
        db.session.merge(financeiro)
        db.session.commit()

    def delete(self, financeiro):
        db.session.delete(financeiro)
        db.session.commit()
