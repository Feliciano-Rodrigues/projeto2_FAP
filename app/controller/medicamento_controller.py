from flask import Blueprint, jsonify, request
from ..entity.medicamento import Medicamento
from ..service.medicamento_service import (
    create_medicamento, get_all_medicamentos, get_medicamento_by_id,
    update_medicamento, delete_medicamento
)
from ..exception.custom_exceptions import EntityNotFound

medicamento_bp = Blueprint('medicamento', __name__)

@medicamento_bp.route('/medicamentos', methods=['GET'])
def get_medicamentos():
    medicamentos = get_all_medicamentos()
    return jsonify([med.to_dict() for med in medicamentos])

@medicamento_bp.route('/medicamentos/<int:id>', methods=['GET'])
def get_medicamento(id):
    try:
        medicamento = get_medicamento_by_id(id)
        return jsonify(medicamento.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Medicamento não encontrado'}), 404

@medicamento_bp.route('/medicamentos', methods=['POST'])
def add_medicamento():
    data = request.get_json()
    try:
        medicamento = create_medicamento(data)
        return jsonify(medicamento.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@medicamento_bp.route('/medicamentos/<int:id>', methods=['PUT'])
def update_medicamento(id):
    data = request.get_json()
    try:
        medicamento = update_medicamento(id, data)
        return jsonify(medicamento.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Medicamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@medicamento_bp.route('/medicamentos/<int:id>', methods=['DELETE'])
def delete_medicamento(id):
    try:
        delete_medicamento(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Medicamento não encontrado'}), 404
