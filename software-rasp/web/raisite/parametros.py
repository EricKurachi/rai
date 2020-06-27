from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, FloatField, SelectField, RadioField
from wtforms.validators import DataRequired

OPER_CHOICES = [('const_flux', "Fluxo Constante"),('const_press',"Pressão Constante")]

class ParamForm(FlaskForm):
    inspiration_volume = FloatField("inspiration_volume", validators=[DataRequired()])
    inspiration_time = FloatField("inspiration_time",  validators=[DataRequired()])
    expiration_time = FloatField("expiration_time",  validators=[DataRequired()])
    o2_fraction = FloatField("o2_fraction", validators=[DataRequired()])
    inspiration_pressure = FloatField("inspiration_pressure", validators=[DataRequired()])
    operation_mode = SelectField("operation_mode", choices=OPER_CHOICES,  validators=[DataRequired()])
