from ..entity.cliente_pessoa import ClientePessoa
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_cliente_pessoa(cliente_pessoa):
    """Salva um novo cliente (pessoa) no banco de dados."""
    db.session.add(cliente_pessoa)
    db.session.commit()
    return cliente_pessoa

def get_all_clientes_pessoas():
    """Retorna todos os clientes (pessoas) do banco de dados."""
    return ClientePessoa.query.all()

def get_cliente_pessoa_by_id(cliente_pessoa_id):
    """Retorna um cliente (pessoa) pelo ID. Levanta EntityNotFound se não for encontrado."""
    cliente_pessoa = ClientePessoa.query.get(cliente_pessoa_id)
    if not cliente_pessoa:
        raise EntityNotFound("ClientePessoa", cliente_pessoa_id)
    return cliente_pessoa

def update_cliente_pessoa(cliente_pessoa_id, data):
    """Atualiza os dados de um cliente (pessoa). Levanta EntityNotFound se não for encontrado."""
    cliente_pessoa = get_cliente_pessoa_by_id(cliente_pessoa_id)
    for key, value in data.items():
        setattr(cliente_pessoa, key, value)
    db.session.commit()
    return cliente_pessoa

def delete_cliente_pessoa(cliente_pessoa_id):
    """Deleta um cliente (pessoa) pelo ID. Levanta EntityNotFound se não for encontrado."""
    cliente_pessoa = get_cliente_pessoa_by_id(cliente_pessoa_id)
    db.session.delete(cliente_pessoa)
    db.session.commit()
