from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, DateField, SubmitField

class CadastroForm(FlaskForm):
    nome = StringField('Nome do Navio')
    loa = FloatField('LOA (metros)')
    boca = FloatField('Boca (metros)')
    dwt = IntegerField('DWT')
    calado_entrada = FloatField('Calado de Entrada (metros)')
    calado_saida = FloatField('Calado de Saída (metros)')
    calado_aereo = FloatField('Calado Aéreo (metros)')
    pontal = FloatField('Pontal (metros)')
    tamanho_lanca = FloatField('Tamanho da Lança (metros)')
    ano_construcao = IntegerField('Ano de Construção')
    tipo_navio = StringField('Tipo de Navio')
    ultimo_porto = StringField('Último Porto')
    proximo_porto = StringField('Próximo Porto')
    data_chegada = DateField('Data de Chegada')
    submit = SubmitField('Enviar')
