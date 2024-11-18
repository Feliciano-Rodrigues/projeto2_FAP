from ..entity.administradores import Administradores
from .. import db
from ..exception.custom_exceptions import EntityNotFound


def save_administradores(administrador):
    """Salva um novo administrador no banco de dados."""
    db.session.add(administrador)
    db.session.commit()
    return administrador

def get_all_administradores():
    """Retorna todos os administradores do banco de dados."""
    return Administradores.query.all()

def get_administradores_by_id(administrador_id):
    """Retorna um administrador pelo ID. Levanta EntityNotFound se não for encontrado."""
    administrador = Administradores.query.get(administrador_id)
    if not administrador:
        raise EntityNotFound("Administradores", administrador_id)
    return administrador

def update_administradores(administrador_id, data):
    """Atualiza os dados de um administrador. Levanta EntityNotFound se não for encontrado."""
    administrador = get_administradores_by_id(administrador_id)
    for key, value in data.items():
        setattr(administrador, key, value)
    db.session.commit()
    return administrador

def delete_administradores(administrador_id):
    """Deleta um administrador pelo ID. Levanta EntityNotFound se não for encontrado."""
    administrador = get_administradores_by_id(administrador_id)
    db.session.delete(administrador)
    db.session.commit()
