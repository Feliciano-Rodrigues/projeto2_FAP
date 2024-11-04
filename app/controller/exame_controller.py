from flask import Blueprint, jsonify, request
from ..entity.exame import Exame
from ..service.exame_service import (
    create_exame, get_all_exames, get_exame_by_id,
    update_exame, delete_exame
)
from ..exception.custom_exceptions import EntityNotFound

exame_bp = Blueprint('exame', __name__)

@exame_bp.route('/exames', methods=['GET'])
def get_exames():
    exames = get_all_exames()
    return jsonify([ex.to_dict() for ex in exames])

@exame_bp.route('/exames/<int:id>', methods=['GET'])
def get_exame(id):
    try:
        exame = get_exame_by_id(id)
        return jsonify(exame.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Exame não encontrado'}), 404

@exame_bp.route('/exames', methods=['POST'])
def add_exame():
    data = request.get_json()
    try:
        exame = create_exame(data)
        return jsonify(exame.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@exame_bp.route('/exames/<int:id>', methods=['PUT'])
def update_exame(id):
    data = request.get_json()
    try:
        exame = update_exame(id, data)
        return jsonify(exame.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Exame não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@exame_bp.route('/exames/<int:id>', methods=['DELETE'])
def delete_exame(id):
    try:
        delete_exame(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Exame não encontrado'}), 404
