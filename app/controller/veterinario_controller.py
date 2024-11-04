from flask import Blueprint, jsonify, request
from ..entity.veterinario import Veterinario
from ..service.veterinario_service import (
    create_veterinario, get_all_veterinarios, get_veterinario_by_id,
    update_veterinario, delete_veterinario
)
from ..exception.custom_exceptions import EntityNotFound

veterinario_bp = Blueprint('veterinario', __name__)

@veterinario_bp.route('/veterinarios', methods=['GET'])
def get_veterinarios():
    veterinarios = get_all_veterinarios()
    return jsonify([vet.to_dict() for vet in veterinarios])

@veterinario_bp.route('/veterinarios/<int:id>', methods=['GET'])
def get_veterinario(id):
    try:
        veterinario = get_veterinario_by_id(id)
        return jsonify(veterinario.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Veterinário não encontrado'}), 404

@veterinario_bp.route('/veterinarios', methods=['POST'])
def add_veterinario():
    data = request.get_json()
    try:
        veterinario = create_veterinario(data)
        return jsonify(veterinario.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@veterinario_bp.route('/veterinarios/<int:id>', methods=['PUT'])
def update_veterinario(id):
    data = request.get_json()
    try:
        veterinario = update_veterinario(id, data)
        return jsonify(veterinario.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Veterinário não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@veterinario_bp.route('/veterinarios/<int:id>', methods=['DELETE'])
def delete_veterinario(id):
    try:
        delete_veterinario(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Veterinário não encontrado'}), 404
