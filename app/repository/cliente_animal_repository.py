from app import db
from ..entity.cliente_animal import ClienteAnimal

class ClienteAnimalRepository:
    def add(self, cliente_animal):
        db.session.add(cliente_animal)
        db.session.commit()

    def get_all(self):
        return ClienteAnimal.query.all()

    def get_by_id(self, id):
        return ClienteAnimal.query.get(id)

    def update(self, cliente_animal):
        db.session.merge(cliente_animal)
        db.session.commit()

    def delete(self, cliente_animal):
        db.session.delete(cliente_animal)
        db.session.commit()
