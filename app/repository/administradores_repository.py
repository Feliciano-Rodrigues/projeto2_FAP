from app import db
from ..entity.administradores import Administradores

class AdministradoresRepository:
    def add(self, administrador):
        db.session.add(administrador)
        db.session.commit()

    def get_all(self):
        return Administradores.query.all()

    def get_by_id(self, id):
        return Administradores.query.get(id)

    def update(self, administrador):
        db.session.merge(administrador)
        db.session.commit()

    def delete(self, administrador):
        db.session.delete(administrador)
        db.session.commit()
