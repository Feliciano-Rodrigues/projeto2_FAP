from ..entity.financeiro import Financeiro
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_financeiro(financeiro):
    """Salva um novo financeiro no banco de dados."""
    db.session.add(financeiro)
    db.session.commit()
    return financeiro

def get_all_financeiros():
    """Retorna todos os financeiros do banco de dados."""
    return Financeiro.query.all()

def get_financeiro_by_id(financeiro_id):
    """Retorna um financeiro pelo ID. Levanta EntityNotFound se não for encontrado."""
    financeiro = Financeiro.query.get(financeiro_id)
    if not financeiro:
        raise EntityNotFound("Financeiro", financeiro_id)
    return financeiro

def update_financeiro(financeiro_id, data):
    """Atualiza os dados de um financeiro. Levanta EntityNotFound se não for encontrado."""
    financeiro = get_financeiro_by_id(financeiro_id)
    for key, value in data.items():
        setattr(financeiro, key, value)
    db.session.commit()
    return financeiro

def delete_financeiro(financeiro_id):
    """Deleta um financeiro pelo ID. Levanta EntityNotFound se não for encontrado."""
    financeiro = get_financeiro_by_id(financeiro_id)
    db.session.delete(financeiro)
    db.session.commit()
