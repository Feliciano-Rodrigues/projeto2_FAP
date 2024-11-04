from flask import Blueprint, jsonify, request
from ..entity.internamento import Internamento
from ..service.internamento_service import (
    create_internamento, get_all_internamentos, get_internamento_by_id,
    update_internamento, delete_internamento
)
from ..exception.custom_exceptions import EntityNotFound

internamento_bp = Blueprint('internamento', __name__)

@internamento_bp.route('/internamentos', methods=['GET'])
def get_internamentos():
    internamentos = get_all_internamentos()
    return jsonify([int.to_dict() for int in internamentos])

@internamento_bp.route('/internamentos/<int:id>', methods=['GET'])
def get_internamento(id):
    try:
        internamento = get_internamento_by_id(id)
        return jsonify(internamento.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Internamento não encontrado'}), 404

@internamento_bp.route('/internamentos', methods=['POST'])
def add_internamento():
    data = request.get_json()
    try:
        internamento = create_internamento(data)
        return jsonify(internamento.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@internamento_bp.route('/internamentos/<int:id>', methods=['PUT'])
def update_internamento(id):
    data = request.get_json()
    try:
        internamento = update_internamento(id, data)
        return jsonify(internamento.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Internamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@internamento_bp.route('/internamentos/<int:id>', methods=['DELETE'])
def delete_internamento(id):
    try:
        delete_internamento(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Internamento não encontrado'}), 404
