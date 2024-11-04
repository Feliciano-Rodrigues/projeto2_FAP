from app import db
from ..entity.auxiliar_veterinario import AuxiliarVeterinario

class AuxiliarVeterinarioRepository:
    def add(self, auxiliar_veterinario):
        db.session.add(auxiliar_veterinario)
        db.session.commit()

    def get_all(self):
        return AuxiliarVeterinario.query.all()

    def get_by_id(self, id):
        return AuxiliarVeterinario.query.get(id)

    def update(self, auxiliar_veterinario):
        db.session.merge(auxiliar_veterinario)
        db.session.commit()

    def delete(self, auxiliar_veterinario):
        db.session.delete(auxiliar_veterinario)
        db.session.commit()
