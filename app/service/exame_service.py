from ..entity.exame import Exame
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_exame(exame):
    """Salva um novo exame no banco de dados."""
    db.session.add(exame)
    db.session.commit()
    return exame

def get_all_exames():
    """Retorna todos os exames do banco de dados."""
    return Exame.query.all()

def get_exame_by_id(exame_id):
    """Retorna um exame pelo ID. Levanta EntityNotFound se não for encontrado."""
    exame = Exame.query.get(exame_id)
    if not exame:
        raise EntityNotFound("Exame", exame_id)
    return exame

def update_exame(exame_id, data):
    """Atualiza os dados de um exame. Levanta EntityNotFound se não for encontrado."""
    exame = get_exame_by_id(exame_id)
    for key, value in data.items():
        setattr(exame, key, value)
    db.session.commit()
    return exame

def delete_exame(exame_id):
    """Deleta um exame pelo ID. Levanta EntityNotFound se não for encontrado."""
    exame = get_exame_by_id(exame_id)
    db.session.delete(exame)
    db.session.commit()
