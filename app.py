from flask import Flask, request, jsonify
from db.controller import VeterinarioController
from app.entity.agenda import Agenda
from app.service.agenda_service import (
    create_agenda, get_all_agendas, get_agenda_by_id,
    update_agenda, delete_agenda
)
from app.exception.custom_exceptions import EntityNotFound

app = Flask(__name__)
veterinario_controller = VeterinarioController()

@app.route('/veterinario', methods=['POST'])
def cadastrar_veterinario():
    data = request.get_json()
    novo_veterinario = veterinario_controller.criar_veterinario(data['nome'], data['especialidade'])
    return jsonify(novo_veterinario), 201

@app.route('/veterinario', methods=['GET'])
def listar_veterinarios():
    veterinarios = veterinario_controller.obter_veterinarios()
    return jsonify(veterinarios), 200

@app.route('/veterinario/<int:veterinario_id>', methods=['PUT'])
def atualizar_veterinario(veterinario_id):
    data = request.get_json()
    resultado = veterinario_controller.modificar_veterinario(veterinario_id, data.get('nome'), data.get('especialidade'))
    return jsonify(resultado), 200

@app.route('/veterinario/<int:veterinario_id>', methods=['DELETE'])
def deletar_veterinario(veterinario_id):
    resultado = veterinario_controller.remover_veterinario(veterinario_id)
    return jsonify({"mensagem": f"Veterinário {resultado} removido com sucesso!"}), 200

# Rotas da Agenda
@app.route('/agendas', methods=['GET'])
def get_agendas():
    agendas = get_all_agendas()
    return jsonify([agd.to_dict() for agd in agendas])

@app.route('/agendas/<int:id>', methods=['GET'])
def get_agenda(id):
    try:
        agenda = get_agenda_by_id(id)
        return jsonify(agenda.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404

@app.route('/agendas', methods=['POST'])
def add_agenda():
    data = request.get_json()
    try:
        agenda = create_agenda(data)
        return jsonify(agenda.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/agendas/<int:id>', methods=['PUT'])
def update_agenda(id):
    data = request.get_json()
    try:
        agenda = update_agenda(id, data)
        return jsonify(agenda.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/agendas/<int:id>', methods=['DELETE'])
def delete_agenda(id):
    try:
        delete_agenda(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
