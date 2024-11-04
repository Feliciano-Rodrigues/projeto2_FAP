from flask import Blueprint, jsonify, request
from ..entity.financeiro import Financeiro
from ..service.financeiro_service import (
    create_financeiro, get_all_financeiros, get_financeiro_by_id,
    update_financeiro, delete_financeiro
)
from ..exception.custom_exceptions import EntityNotFound

financeiro_bp = Blueprint('financeiro', __name__)

@financeiro_bp.route('/financeiros', methods=['GET'])
def get_financeiros():
    financeiros = get_all_financeiros()
    return jsonify([fin.to_dict() for fin in financeiros])

@financeiro_bp.route('/financeiros/<int:id>', methods=['GET'])
def get_financeiro(id):
    try:
        financeiro = get_financeiro_by_id(id)
        return jsonify(financeiro.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Financeiro não encontrado'}), 404

@financeiro_bp.route('/financeiros', methods=['POST'])
def add_financeiro():
    data = request.get_json()
    try:
        financeiro = create_financeiro(data)
        return jsonify(financeiro.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@financeiro_bp.route('/financeiros/<int:id>', methods=['PUT'])
def update_financeiro(id):
    data = request.get_json()
    try:
        financeiro = update_financeiro(id, data)
        return jsonify(financeiro.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Financeiro não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@financeiro_bp.route('/financeiros/<int:id>', methods=['DELETE'])
def delete_financeiro(id):
    try:
        delete_financeiro(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Financeiro não encontrado'}), 404
