from ..entity.funcionario import Funcionario
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_funcionario(funcionario):
    """Salva um novo funcionário no banco de dados."""
    db.session.add(funcionario)
    db.session.commit()
    return funcionario

def get_all_funcionarios():
    """Retorna todos os funcionários do banco de dados."""
    return Funcionario.query.all()

def get_funcionario_by_id(funcionario_id):
    """Retorna um funcionário pelo ID. Levanta EntityNotFound se não for encontrado."""
    funcionario = Funcionario.query.get(funcionario_id)
    if not funcionario:
        raise EntityNotFound("Funcionario", funcionario_id)
    return funcionario

def update_funcionario(funcionario_id, data):
    """Atualiza os dados de um funcionário. Levanta EntityNotFound se não for encontrado."""
    funcionario = get_funcionario_by_id(funcionario_id)
    for key, value in data.items():
        setattr(funcionario, key, value)
    db.session.commit()
    return funcionario

def delete_funcionario(funcionario_id):
    """Deleta um funcionário pelo ID. Levanta EntityNotFound se não for encontrado."""
    funcionario = get_funcionario_by_id(funcionario_id)
    db.session.delete(funcionario)
    db.session.commit()
