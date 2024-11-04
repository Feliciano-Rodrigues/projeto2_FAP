from ..entity.medicamento import Medicamento
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_medicamento(medicamento):
    """Salva um novo medicamento no banco de dados."""
    db.session.add(medicamento)
    db.session.commit()
    return medicamento

def get_all_medicamentos():
    """Retorna todos os medicamentos do banco de dados."""
    return Medicamento.query.all()

def get_medicamento_by_id(medicamento_id):
    """Retorna um medicamento pelo ID. Levanta EntityNotFound se não for encontrado."""
    medicamento = Medicamento.query.get(medicamento_id)
    if not medicamento:
        raise EntityNotFound("Medicamento", medicamento_id)
    return medicamento

def update_medicamento(medicamento_id, data):
    """Atualiza os dados de um medicamento. Levanta EntityNotFound se não for encontrado."""
    medicamento = get_medicamento_by_id(medicamento_id)
    for key, value in data.items():
        setattr(medicamento, key, value)
    db.session.commit()
    return medicamento

def delete_medicamento(medicamento_id):
    """Deleta um medicamento pelo ID. Levanta EntityNotFound se não for encontrado."""
    medicamento = get_medicamento_by_id(medicamento_id)
    db.session.delete(medicamento)
    db.session.commit()
