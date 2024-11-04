from app import db
from datetime import datetime

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id_funcionario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True)
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(255))
    data_nascimento = db.Column(db.Date)
    veterinario = db.relationship('Veterinario', backref='funcionario', uselist=False)
    auxiliar_veterinario = db.relationship('AuxiliarVeterinario', backref='funcionario', uselist=False)
    administradores = db.relationship('Administradores', backref='funcionario', uselist=False)

class Veterinario(db.Model):
    __tablename__ = 'veterinario'
    id_veterinario = db.Column(db.Integer, primary_key=True)
    crmv = db.Column(db.String(20), unique=True, nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'))

class AuxiliarVeterinario(db.Model):
    __tablename__ = 'auxiliar_veterinario'
    id_auxiliar = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(128))
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'))

class Administradores(db.Model):
    __tablename__ = 'administradores'
    id_admin = db.Column(db.Integer, primary_key=True)
    setor = db.Column(db.String(128))
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'))

class ClientePessoa(db.Model):
    __tablename__ = 'cliente_pessoa'
    id_cliente_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(20))

class ClienteAnimal(db.Model):
    __tablename__ = 'cliente_animal'
    id_cliente_animal = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    especie = db.Column(db.String(50))
    raca = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    dono_id = db.Column(db.Integer, db.ForeignKey('cliente_pessoa.id_cliente_pessoa'))
    dono = db.relationship('ClientePessoa', backref='animais')

class Cirurgia(db.Model):
    __tablename__ = 'cirurgia'
    id_cirurgia = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinario.id_veterinario'))

class Consulta(db.Model):
    __tablename__ = 'consulta'
    id_consulta = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinario.id_veterinario'))
    cliente_animal_id = db.Column(db.Integer, db.ForeignKey('cliente_animal.id_cliente_animal'))

class Prescricao(db.Model):
    __tablename__ = 'prescricao'
    id_prescricao = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'))

class Internamento(db.Model):
    __tablename__ = 'internamento'
    id_internamento = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date)
    cliente_animal_id = db.Column(db.Integer, db.ForeignKey('cliente_animal.id_cliente_animal'))

class Agenda(db.Model):
    __tablename__ = 'agenda'
    id_agenda = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinario.id_veterinario'))

class Exame(db.Model):
    __tablename__ = 'exame'
    id_exame = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(128), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255))
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'))

class Medicamento(db.Model):
    __tablename__ = 'medicamento'
    id_medicamento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    fabricante = db.Column(db.String(128))
    lote = db.Column(db.String(128))

class Financeiro(db.Model):
    __tablename__ = 'financeiro'
    id_financeiro = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255))

# Adicionar representações em dicionário (to_dict) para facilitar a conversão para JSON
def to_dict(self):
    return {col.name: getattr(self, col.name) for col in self.__table__.columns}

# Adicionar o método to_dict às classes
Funcionario.to_dict = to_dict
Veterinario.to_dict = to_dict
AuxiliarVeterinario.to_dict = to_dict
Administradores.to_dict = to_dict
ClientePessoa.to_dict = to_dict
ClienteAnimal.to_dict = to_dict
Cirurgia.to_dict = to_dict
Consulta.to_dict = to_dict
Prescricao.to_dict = to_dict
Internamento.to_dict = to_dict
Agenda.to_dict = to_dict
Exame.to_dict = to_dict
Medicamento.to_dict = to_dict
Financeiro.to_dict = to_dict
