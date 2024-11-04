from ..entity.consulta import Consulta
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_consulta(consulta):
    """Salva uma nova consulta no banco de dados."""
    db.session.add(consulta)
    db.session.commit()
    return consulta

def get_all_consultas():
    """Retorna todas as consultas do banco de dados."""
    return Consulta.query.all()

def get_consulta_by_id(consulta_id):
    """Retorna uma consulta pelo ID. Levanta EntityNotFound se não for encontrada."""
    consulta = Consulta.query.get(consulta_id)
    if not consulta:
        raise EntityNotFound("Consulta", consulta_id)
    return consulta

def update_consulta(consulta_id, data):
    """Atualiza os dados de uma consulta. Levanta EntityNotFound se não for encontrada."""
    consulta = get_consulta_by_id(consulta_id)
    for key, value in data.items():
        setattr(consulta, key, value)
    db.session.commit()
    return consulta

def delete_consulta(consulta_id):
    """Deleta uma consulta pelo ID. Levanta EntityNotFound se não for encontrada."""
    consulta = get_consulta_by_id(consulta_id)
    db.session.delete(consulta)
    db.session.commit()
