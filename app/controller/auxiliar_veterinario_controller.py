from flask import Blueprint, jsonify, request
from ..entity.auxiliar_veterinario import AuxiliarVeterinario
from ..service.auxiliar_veterinario_service import (
    create_auxiliar_veterinario, get_all_auxiliar_veterinarios, get_auxiliar_veterinario_by_id,
    update_auxiliar_veterinario, delete_auxiliar_veterinario
)
from ..exception.custom_exceptions import EntityNotFound

auxiliar_veterinario_bp = Blueprint('auxiliar_veterinario', __name__)

@auxiliar_veterinario_bp.route('/auxiliar_veterinarios', methods=['GET'])
def get_auxiliar_veterinarios():
    auxiliares = get_all_auxiliar_veterinarios()
    return jsonify([aux.to_dict() for aux in auxiliares])

@auxiliar_veterinario_bp.route('/auxiliar_veterinarios/<int:id>', methods=['GET'])
def get_auxiliar_veterinario(id):
    try:
        auxiliar = get_auxiliar_veterinario_by_id(id)
        return jsonify(auxiliar.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Auxiliar Veterinário não encontrado'}), 404

@auxiliar_veterinario_bp.route('/auxiliar_veterinarios', methods=['POST'])
def add_auxiliar_veterinario():
    data = request.get_json()
    try:
        auxiliar = create_auxiliar_veterinario(data)
        return jsonify(auxiliar.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auxiliar_veterinario_bp.route('/auxiliar_veterinarios/<int:id>', methods=['PUT'])
def update_auxiliar_veterinario(id):
    data = request.get_json()
    try:
        auxiliar = update_auxiliar_veterinario(id, data)
        return jsonify(auxiliar.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Auxiliar Veterinário não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auxiliar_veterinario_bp.route('/auxiliar_veterinarios/<int:id>', methods=['DELETE'])
def delete_auxiliar_veterinario(id):
    try:
        delete_auxiliar_veterinario(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Auxiliar Veterinário não encontrado'}), 404
