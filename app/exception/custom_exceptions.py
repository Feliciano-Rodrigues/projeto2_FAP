class EntityNotFound(Exception):
    """Exceção levantada quando uma entidade não é encontrada no banco de dados."""
    def __init__(self, entity, entity_id):
        self.entity = entity
        self.entity_id = entity_id
        super().__init__(f"{entity} com ID {entity_id} não foi encontrado.")

class InvalidData(Exception):
    """Exceção levantada quando os dados fornecidos são inválidos."""
    def __init__(self, message="Dados inválidos fornecidos"):
        self.message = message
        super().__init__(self.message)
