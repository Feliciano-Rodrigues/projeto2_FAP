from flask import Blueprint, jsonify, request
from ..entity.cliente_pessoa import ClientePessoa
from ..service.cliente_pessoa_service import (
    create_cliente_pessoa, get_all_clientes_pessoas, get_cliente_pessoa_by_id,
    update_cliente_pessoa, delete_cliente_pessoa
)
from ..exception.custom_exceptions import EntityNotFound

cliente_pessoa_bp = Blueprint('cliente_pessoa', __name__)

@cliente_pessoa_bp.route('/clientes_pessoas', methods=['GET'])
def get_clientes_pessoas():
    clientes_pessoas = get_all_clientes_pessoas()
    return jsonify([cli.to_dict() for cli in clientes_pessoas])

@cliente_pessoa_bp.route('/clientes_pessoas/<int:id>', methods=['GET'])
def get_cliente_pessoa(id):
    try:
        cliente_pessoa = get_cliente_pessoa_by_id(id)
        return jsonify(cliente_pessoa.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cliente (pessoa) não encontrado'}), 404

@cliente_pessoa_bp.route('/clientes_pessoas', methods=['POST'])
def add_cliente_pessoa():
    data = request.get_json()
    try:
        cliente_pessoa = create_cliente_pessoa(data)
        return jsonify(cliente_pessoa.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cliente_pessoa_bp.route('/clientes_pessoas/<int:id>', methods=['PUT'])
def update_cliente_pessoa(id):
    data = request.get_json()
    try:
        cliente_pessoa = update_cliente_pessoa(id, data)
        return jsonify(cliente_pessoa.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Cliente (pessoa) não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cliente_pessoa_bp.route('/clientes_pessoas/<int:id>', methods=['DELETE'])
def delete_cliente_pessoa(id):
    try:
        delete_cliente_pessoa(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Cliente (pessoa) não encontrado'}), 404
