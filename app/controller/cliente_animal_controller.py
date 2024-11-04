from flask import Blueprint, jsonify, request
from ..entity.cliente_animal import ClienteAnimal
from ..service.cliente_animal_service import (
    create_cliente_animal, get_all_clientes_animais, get_cliente_animal_by_id,
    update_cliente_animal, delete_cliente_animal
)
from ..exception.custom_exceptions import EntityNotFound

cliente_animal_bp = Blueprint('cliente_animal', __name__)

@cliente_animal_bp.route('/clientes_animais', methods=['GET'])
def get_clientes_animais():
    clientes_animais = get_all_clientes_animais()
    return jsonify([cli.to_dict() for cli in clientes_animais])

@cliente_animal_bp.route('/clientes_animais/<int:id>', methods=['GET'])
def get_cliente_animal(id):
    try:
        cliente_animal = get_cliente_animal_by_id(id)
        return jsonify(cliente_animal.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cliente (animal) não encontrado'}), 404

@cliente_animal_bp.route('/clientes_animais', methods=['POST'])
def add_cliente_animal():
    data = request.get_json()
    try:
        cliente_animal = create_cliente_animal(data)
        return jsonify(cliente_animal.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cliente_animal_bp.route('/clientes_animais/<int:id>', methods=['PUT'])
def update_cliente_animal(id):
    data = request.get_json()
    try:
        cliente_animal = update_cliente_animal(id, data)
        return jsonify(cliente_animal.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cliente (animal) não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cliente_animal_bp.route('/clientes_animais/<int:id>', methods=['DELETE'])
def delete_cliente_animal(id):
    try:
        delete_cliente_animal(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Cliente (animal) não encontrado'}), 404
