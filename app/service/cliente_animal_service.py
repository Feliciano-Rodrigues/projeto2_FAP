from ..entity.cliente_animal import ClienteAnimal
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_cliente_animal(cliente_animal):
    """Salva um novo cliente (animal) no banco de dados."""
    db.session.add(cliente_animal)
    db.session.commit()
    return cliente_animal

def get_all_clientes_animais():
    """Retorna todos os clientes (animais) do banco de dados."""
    return ClienteAnimal.query.all()

def get_cliente_animal_by_id(cliente_animal_id):
    """Retorna um cliente (animal) pelo ID. Levanta EntityNotFound se não for encontrado."""
    cliente_animal = ClienteAnimal.query.get(cliente_animal_id)
    if not cliente_animal:
        raise EntityNotFound("ClienteAnimal", cliente_animal_id)
    return cliente_animal

def update_cliente_animal(cliente_animal_id, data):
    """Atualiza os dados de um cliente (animal). Levanta EntityNotFound se não for encontrado."""
    cliente_animal = get_cliente_animal_by_id(cliente_animal_id)
    for key, value in data.items():
        setattr(cliente_animal, key, value)
    db.session.commit()
    return cliente_animal

def delete_cliente_animal(cliente_animal_id):
    """Deleta um cliente (animal) pelo ID. Levanta EntityNotFound se não for encontrado."""
    cliente_animal = get_cliente_animal_by_id(cliente_animal_id)
    db.session.delete(cliente_animal)
    db.session.commit()
