from flask import Blueprint, jsonify, request
from ..entity.consulta import Consulta
from ..service.consulta_service import (
    create_consulta, get_all_consultas, get_consulta_by_id,
    update_consulta, delete_consulta
)
from ..exception.custom_exceptions import EntityNotFound

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consultas', methods=['GET'])
def get_consultas():
    consultas = get_all_consultas()
    return jsonify([con.to_dict() for con in consultas])

@consulta_bp.route('/consultas/<int:id>', methods=['GET'])
def get_consulta(id):
    try:
        consulta = get_consulta_by_id(id)
        return jsonify(consulta.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Consulta não encontrada'}), 404

@consulta_bp.route('/consultas', methods=['POST'])
def add_consulta():
    data = request.get_json()
    try:
        consulta = create_consulta(data)
        return jsonify(consulta.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@consulta_bp.route('/consultas/<int:id>', methods=['PUT'])
def update_consulta(id):
    data = request.get_json()
    try:
        consulta = update_consulta(id, data)
        return jsonify(consulta.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Consulta não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@consulta_bp.route('/consultas/<int:id>', methods=['DELETE'])
def delete_consulta(id):
    try:
        delete_consulta(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Consulta não encontrada'}), 404
