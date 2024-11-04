from flask import Blueprint, jsonify, request
from ..entity.prescricao import Prescricao
from ..service.prescricao_service import (
    create_prescricao, get_all_prescricoes, get_prescricao_by_id,
    update_prescricao, delete_prescricao
)
from ..exception.custom_exceptions import EntityNotFound

prescricao_bp = Blueprint('prescricao', __name__)

@prescricao_bp.route('/prescricoes', methods=['GET'])
def get_prescricoes():
    prescricoes = get_all_prescricoes()
    return jsonify([pre.to_dict() for pre in prescricoes])

@prescricao_bp.route('/prescricoes/<int:id>', methods=['GET'])
def get_prescricao(id):
    try:
        prescricao = get_prescricao_by_id(id)
        return jsonify(prescricao.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Prescrição não encontrada'}), 404

@prescricao_bp.route('/prescricoes', methods=['POST'])
def add_prescricao():
    data = request.get_json()
    try:
        prescricao = create_prescricao(data)
        return jsonify(prescricao.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@prescricao_bp.route('/prescricoes/<int:id>', methods=['PUT'])
def update_prescricao(id):
    data = request.get_json()
    try:
        prescricao = update_prescricao(id, data)
        return jsonify(prescricao.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Prescrição não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@prescricao_bp.route('/prescricoes/<int:id>', methods=['DELETE'])
def delete_prescricao(id):
    try:
        delete_prescricao(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Prescrição não encontrada'}), 404
