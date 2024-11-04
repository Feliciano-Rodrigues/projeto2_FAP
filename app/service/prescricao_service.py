from ..entity.prescricao import Prescricao
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_prescricao(prescricao):
    """Salva uma nova prescrição no banco de dados."""
    db.session.add(prescricao)
    db.session.commit()
    return prescricao

def get_all_prescricoes():
    """Retorna todas as prescrições do banco de dados."""
    return Prescricao.query.all()

def get_prescricao_by_id(prescricao_id):
    """Retorna uma prescrição pelo ID. Levanta EntityNotFound se não for encontrada."""
    prescricao = Prescricao.query.get(prescricao_id)
    if not prescricao:
        raise EntityNotFound("Prescricao", prescricao_id)
    return prescricao

def update_prescricao(prescricao_id, data):
    """Atualiza os dados de uma prescrição. Levanta EntityNotFound se não for encontrada."""
    prescricao = get_prescricao_by_id(prescricao_id)
    for key, value in data.items():
        setattr(prescricao, key, value)
    db.session.commit()
    return prescricao

def delete_prescricao(prescricao_id):
    """Deleta uma prescrição pelo ID. Levanta EntityNotFound se não for encontrada."""
    prescricao = get_prescricao_by_id(prescricao_id)
    db.session.delete(prescricao)
    db.session.commit()
