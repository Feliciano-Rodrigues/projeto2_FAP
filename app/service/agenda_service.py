from app.entity.agenda import Agenda
from app import db
from app.exception.custom_exceptions import EntityNotFound

def save_agenda(agenda):
    db.session.add(agenda)
    db.session.commit()
    return agenda

def get_all_agendas():
    return Agenda.query.all()

def get_agenda_by_id(agenda_id):
    agenda = Agenda.query.get(agenda_id)
    if not agenda:
        raise EntityNotFound("Agenda", agenda_id)
    return agenda

def update_agenda(agenda_id, data):
    agenda = get_agenda_by_id(agenda_id)
    for key, value in data.items():
        setattr(agenda, key, value)
    db.session.commit()
    return agenda

def delete_agenda(agenda_id):
    agenda = get_agenda_by_id(agenda_id)
    db.session.delete(agenda)
    db.session.commit()

def create_agenda(data):
    agenda = Agenda(
        titulo=data.get('titulo'),
        data=data.get('data'),
        descricao=data.get('descricao')
    )
    return save_agenda(agenda)
