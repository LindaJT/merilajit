from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, FloatField
from wtforms import SelectField
from datetime import date

class ObsForm(FlaskForm):
    description = StringField("Havainnon kuvaus: ")
    date = DateField(label='Havainnon päivämäärä: ', format = '%d-%m-%Y')
    ncoordinates = FloatField("Pohjoiskoordinaatti:")
    ecoordinates = FloatField("Itäkoordinaatti: ")

    class Meta:
        csrf = False