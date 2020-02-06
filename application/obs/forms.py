from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, FloatField
from wtforms import SelectField
from wtforms.fields.html5 import DateField
from datetime import date

class ObsForm(FlaskForm):
    description = StringField("Havainnon kuvaus: ")
    date = DateField(label='Havainnon päivämäärä: ')
    ncoordinates = FloatField("Pohjoiskoordinaatti:")
    ecoordinates = FloatField("Itäkoordinaatti: ")

    class Meta:
        csrf = False