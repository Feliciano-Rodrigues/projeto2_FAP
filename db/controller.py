# db/controller.py

# Simulação de um "banco de dados" em memória para armazenar dados dos veterinários
veterinarios_db = []

def cadastrar_veterinario(nome, especialidade):
    """Função para cadastrar um novo veterinário"""
    veterinario = {
        'id': len(veterinarios_db) + 1,
        'nome': nome,
        'especialidade': especialidade
    }
    veterinarios_db.append(veterinario)
    return veterinario  # Retorna o veterinário cadastrado

def listar_veterinarios():
    """Função para listar todos os veterinários cadastrados"""
    return veterinarios_db if veterinarios_db else "Nenhum veterinário cadastrado."

def atualizar_veterinario(veterinario_id, nome=None, especialidade=None):
    """Função para atualizar as informações de um veterinário existente"""
    for veterinario in veterinarios_db:
        if veterinario['id'] == veterinario_id:
            if nome:
                veterinario['nome'] = nome
            if especialidade:
                veterinario['especialidade'] = especialidade
            return veterinario  # Retorna o veterinário atualizado
    return None  # Retorna None se o veterinário não for encontrado

def deletar_veterinario(veterinario_id):
    """Função para remover um veterinário do cadastro"""
    global veterinarios_db
    veterinarios_db = [vet for vet in veterinarios_db if vet['id'] != veterinario_id]
    return veterinario_id  # Retorna o ID do veterinário removido

# Controller para interagir com a API
class VeterinarioController:
    def criar_veterinario(self, nome, especialidade):
        return cadastrar_veterinario(nome, especialidade)

    def obter_veterinarios(self):
        return listar_veterinarios()

    def modificar_veterinario(self, veterinario_id, nome=None, especialidade=None):
        resultado = atualizar_veterinario(veterinario_id, nome, especialidade)
        return resultado if resultado else "Veterinário não encontrado."

    def remover_veterinario(self, veterinario_id):
        return deletar_veterinario(veterinario_id)
