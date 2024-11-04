from flask import Blueprint, jsonify, request
from app.entity.agenda import Agenda
from app.service.agenda_service import (
    create_agenda, get_all_agendas, get_agenda_by_id,
    update_agenda, delete_agenda
)
from app.exception.custom_exceptions import EntityNotFound

agenda_bp = Blueprint('agenda', __name__)

@agenda_bp.route('/agendas', methods=['GET'])
def get_agendas():
    agendas = get_all_agendas()
    return jsonify([agd.to_dict() for agd in agendas])

@agenda_bp.route('/agendas/<int:id>', methods=['GET'])
def get_agenda(id):
    try:
        agenda = get_agenda_by_id(id)
        return jsonify(agenda.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404

@agenda_bp.route('/agendas', methods=['POST'])
def add_agenda():
    data = request.get_json()
    try:
        agenda = create_agenda(data)
        return jsonify(agenda.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@agenda_bp.route('/agendas/<int:id>', methods=['PUT'])
def update_agenda(id):
    data = request.get_json()
    try:
        agenda = update_agenda(id, data)
        return jsonify(agenda.to_dict())
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@agenda_bp.route('/agendas/<int:id>', methods=['DELETE'])
def delete_agenda(id):
    try:
        delete_agenda(id)
        return '', 204
    except EntityNotFound:
        return jsonify({'error': 'Agenda não encontrada'}), 404
