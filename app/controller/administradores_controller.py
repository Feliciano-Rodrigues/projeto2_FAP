from flask import Blueprint, jsonify, request
from ..entity.administradores import Administradores
from ..service.administradores_service import (
    create_administradores, get_all_administradores, get_administradores_by_id,
    update_administradores, delete_administradores
)
from ..exception.custom_exceptions import EntityNotFound

administradores_bp = Blueprint('administradores', __name__)

@administradores_bp.route('/administradores', methods=['GET'])
def get_administradores():
    administradores = get_all_administradores()
    return jsonify([adm.to_dict() for adm in administradores])

@administradores_bp.route('/administradores/<int:id>', methods=['GET'])
def get_administrador(id):
    try:
        administrador = get_administradores_by_id(id)
        return jsonify(administrador.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Administrador não encontrado'}), 404

@administradores_bp.route('/administradores', methods=['POST'])
def add_administrador():
    data = request.get_json()
    try:
        administrador = create_administradores(data)
        return jsonify(administrador.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@administradores_bp.route('/administradores/<int:id>', methods=['PUT'])
def update_administrador(id):
    data = request.get_json()
    try:
        administrador = update_administradores(id, data)
        return jsonify(administrador.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Administrador não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@administradores_bp.route('/administradores/<int:id>', methods=['DELETE'])
def delete_administrador(id):
    try:
        delete_administradores(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Administrador não encontrado'}), 404
