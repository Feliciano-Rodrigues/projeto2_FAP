from app import db
from ..entity.cliente_pessoa import ClientePessoa

class ClientePessoaRepository:
    def add(self, cliente_pessoa):
        db.session.add(cliente_pessoa)
        db.session.commit()

    def get_all(self):
        return ClientePessoa.query.all()

    def get_by_id(self, id):
        return ClientePessoa.query.get(id)

    def update(self, cliente_pessoa):
        db.session.merge(cliente_pessoa)
        db.session.commit()

    def delete(self, cliente_pessoa):
        db.session.delete(cliente_pessoa)
        db.session.commit()
