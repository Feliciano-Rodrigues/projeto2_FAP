from ..entity.veterinario import Veterinario
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_veterinario(veterinario):
    """Salva um novo veterinário no banco de dados."""
    db.session.add(veterinario)
    db.session.commit()
    return veterinario

def get_all_veterinarios():
    """Retorna todos os veterinários do banco de dados."""
    return Veterinario.query.all()

def get_veterinario_by_id(veterinario_id):
    """Retorna um veterinário pelo ID. Levanta EntityNotFound se não for encontrado."""
    veterinario = Veterinario.query.get(veterinario_id)
    if not veterinario:
        raise EntityNotFound("Veterinario", veterinario_id)
    return veterinario

def update_veterinario(veterinario_id, data):
    """Atualiza os dados de um veterinário. Levanta EntityNotFound se não for encontrado."""
    veterinario = get_veterinario_by_id(veterinario_id)
    for key, value in data.items():
        setattr(veterinario, key, value)
    db.session.commit()
    return veterinario

def delete_veterinario(veterinario_id):
    """Deleta um veterinário pelo ID. Levanta EntityNotFound se não for encontrado."""
    veterinario = get_veterinario_by_id(veterinario_id)
    db.session.delete(veterinario)
    db.session.commit()
