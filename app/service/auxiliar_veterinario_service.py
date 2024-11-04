from ..entity.auxiliar_veterinario import AuxiliarVeterinario
from .. import db
from ..exception.custom_exceptions import EntityNotFound

def save_auxiliar_veterinario(auxiliar_veterinario):
    """Salva um novo auxiliar veterinário no banco de dados."""
    db.session.add(auxiliar_veterinario)
    db.session.commit()
    return auxiliar_veterinario

def get_all_auxiliar_veterinarios():
    """Retorna todos os auxiliares veterinários do banco de dados."""
    return AuxiliarVeterinario.query.all()

def get_auxiliar_veterinario_by_id(auxiliar_veterinario_id):
    """Retorna um auxiliar veterinário pelo ID. Levanta EntityNotFound se não for encontrado."""
    auxiliar_veterinario = AuxiliarVeterinario.query.get(auxiliar_veterinario_id)
    if not auxiliar_veterinario:
        raise EntityNotFound("AuxiliarVeterinario", auxiliar_veterinario_id)
    return auxiliar_veterinario

def update_auxiliar_veterinario(auxiliar_veterinario_id, data):
    """Atualiza os dados de um auxiliar veterinário. Levanta EntityNotFound se não for encontrado."""
    auxiliar_veterinario = get_auxiliar_veterinario_by_id(auxiliar_veterinario_id)
    for key, value in data.items():
        setattr(auxiliar_veterinario, key, value)
    db.session.commit()
    return auxiliar_veterinario

def delete_auxiliar_veterinario(auxiliar_veterinario_id):
    """Deleta um auxiliar veterinário pelo ID. Levanta EntityNotFound se não for encontrado."""
    auxiliar_veterinario = get_auxiliar_veterinario_by_id(auxiliar_veterinario_id)
    db.session.delete(auxiliar_veterinario)
    db.session.commit()
