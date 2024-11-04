from flask import Blueprint, jsonify, request
from ..entity.cirurgia import Cirurgia
from ..service.cirurgia_service import (
    create_cirurgia, get_all_cirurgias, get_cirurgia_by_id,
    update_cirurgia, delete_cirurgia
)
from ..exception.custom_exceptions import EntityNotFound

cirurgia_bp = Blueprint('cirurgia', __name__)

@cirurgia_bp.route('/cirurgias', methods=['GET'])
def get_cirurgias():
    cirurgias = get_all_cirurgias()
    return jsonify([cir.to_dict() for cir in cirurgias])

@cirurgia_bp.route('/cirurgias/<int:id>', methods=['GET'])
def get_cirurgia(id):
    try:
        cirurgia = get_cirurgia_by_id(id)
        return jsonify(cirurgia.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cirurgia não encontrada'}), 404

@cirurgia_bp.route('/cirurgias', methods=['POST'])
def add_cirurgia():
    data = request.get_json()
    try:
        cirurgia = create_cirurgia(data)
        return jsonify(cirurgia.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cirurgia_bp.route('/cirurgias/<int:id>', methods=['PUT'])
def update_cirurgia(id):
    data = request.get_json()
    try:
        cirurgia = update_cirurgia(id, data)
        return jsonify(cirurgia.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cirurgia não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cirurgia_bp.route('/cirurgias/<int:id>', methods=['DELETE'])
def delete_cirurgia(id):
    try:
        delete_cirurgia(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Cirurgia não encontrada'}), 404
