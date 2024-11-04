from ..entity.internamento import Internamento
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_internamento(internamento):
    """Salva um novo internamento no banco de dados."""
    db.session.add(internamento)
    db.session.commit()
    return internamento

def get_all_internamentos():
    """Retorna todos os internamentos do banco de dados."""
    return Internamento.query.all()

def get_internamento_by_id(internamento_id):
    """Retorna um internamento pelo ID. Levanta EntityNotFound se não for encontrado."""
    internamento = Internamento.query.get(internamento_id)
    if not internamento:
        raise EntityNotFound("Internamento", internamento_id)
    return internamento

def update_internamento(internamento_id, data):
    """Atualiza os dados de um internamento. Levanta EntityNotFound se não for encontrado."""
    internamento = get_internamento_by_id(internamento_id)
    for key, value in data.items():
        setattr(internamento, key, value)
    db.session.commit()
    return internamento

def delete_internamento(internamento_id):
    """Deleta um internamento pelo ID. Levanta EntityNotFound se não for encontrado."""
    internamento = get_internamento_by_id(internamento_id)
    db.session.delete(internamento)
    db.session.commit()
