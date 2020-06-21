from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, FloatField, SelectField, RadioField
from wtforms.validators import DataRequired

GENDER_CHOICES = [('fem', "Feminino"),('masc',"Masculino")]

class TabForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    weight = FloatField("weight",  validators=[DataRequired()])
    height = FloatField("height",  validators=[DataRequired()])
    gender = SelectField("gender", choices=GENDER_CHOICES,  validators=[DataRequired()])
