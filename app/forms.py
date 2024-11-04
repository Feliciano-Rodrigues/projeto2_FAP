from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class FuncionarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=128)])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=128)])
    telefone = StringField('Telefone')
    endereco = StringField('Endereço')
    data_nascimento = StringField('Data de Nascimento')
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Submit')
