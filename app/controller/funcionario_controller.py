from flask import Blueprint, jsonify, request
from ..entity.funcionario import Funcionario
from ..service.funcionario_service import (
    create_funcionario, get_all_funcionarios, get_funcionario_by_id,
    update_funcionario, delete_funcionario
)
from ..exception.custom_exceptions import EntityNotFound

funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    funcionarios = get_all_funcionarios()
    return jsonify([func.to_dict() for func in funcionarios])

@funcionario_bp.route('/funcionarios/<int:id>', methods=['GET'])
def get_funcionario(id):
    try:
        funcionario = get_funcionario_by_id(id)
        return jsonify(funcionario.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Funcionario not found'}), 404

@funcionario_bp.route('/funcionarios', methods=['POST'])
def add_funcionario():
    data = request.get_json()
    try:
        funcionario = create_funcionario(data)
        return jsonify(funcionario.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@funcionario_bp.route('/funcionarios/<int:id>', methods=['PUT'])
def update_funcionario(id):
    data = request.get_json()
    try:
        funcionario = update_funcionario(id, data)
        return jsonify(funcionario.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Funcionario not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@funcionario_bp.route('/funcionarios/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    try:
        delete_funcionario(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Funcionario not found'}), 404
