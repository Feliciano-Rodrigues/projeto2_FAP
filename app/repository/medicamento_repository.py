from app import db
from ..entity.medicamento import Medicamento

class MedicamentoRepository:
    def add(self, medicamento):
        db.session.add(medicamento)
        db.session.commit()

    def get_all(self):
        return Medicamento.query.all()

    def get_by_id(self, id):
        return Medicamento.query.get(id)

    def update(self, medicamento):
        db.session.merge(medicamento)
        db.session.commit()

    def delete(self, medicamento):
        db.session.delete(medicamento)
        db.session.commit()
