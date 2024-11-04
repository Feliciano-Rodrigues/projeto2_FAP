from app.models import Funcionario, db
import bcrypt

def save_funcionario(funcionario):
    db.session.add(funcionario)
    db.session.commit()

def get_all_funcionarios():
    return Funcionario.query.all()

def get_funcionario_by_id(id):
    return Funcionario.query.get(id)

def update_funcionario(id, data):
    funcionario = Funcionario.query.get(id)
    for key, value in data.items():
        setattr(funcionario, key, value)
    db.session.commit()

def delete_funcionario(id):
    funcionario = Funcionario.query.get(id)
    db.session.delete(funcionario)
    db.session.commit()

def hash_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt)
