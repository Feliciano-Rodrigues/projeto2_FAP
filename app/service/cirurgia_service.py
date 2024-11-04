from ..entity.cirurgia import Cirurgia
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_cirurgia(cirurgia):
    """Salva uma nova cirurgia no banco de dados."""
    db.session.add(cirurgia)
    db.session.commit()
    return cirurgia

def get_all_cirurgias():
    """Retorna todas as cirurgias do banco de dados."""
    return Cirurgia.query.all()

def get_cirurgia_by_id(cirurgia_id):
    """Retorna uma cirurgia pelo ID. Levanta EntityNotFound se não for encontrada."""
    cirurgia = Cirurgia.query.get(cirurgia_id)
    if not cirurgia:
        raise EntityNotFound("Cirurgia", cirurgia_id)
    return cirurgia

def update_cirurgia(cirurgia_id, data):
    """Atualiza os dados de uma cirurgia. Levanta EntityNotFound se não for encontrada."""
    cirurgia = get_cirurgia_by_id(cirurgia_id)
    for key, value in data.items():
        setattr(cirurgia, key, value)
    db.session.commit()
    return cirurgia

def delete_cirurgia(cirurgia_id):
    """Deleta uma cirurgia pelo ID. Levanta EntityNotFound se não for encontrada."""
    cirurgia = get_cirurgia_by_id(cirurgia_id)
    db.session.delete(cirurgia)
    db.session.commit()
