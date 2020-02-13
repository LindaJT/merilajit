from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, FloatField
from wtforms import SelectField
from wtforms.fields.html5 import DateField
from datetime import date

class ObsForm(FlaskForm):
    description = StringField("Havainnon kuvaus: ", [validators.Length(min=2, max=200)])
    date = DateField(label="Havainnon päivämäärä: ")
    ncoordinates = FloatField("Pohjoiskoordinaatti:", [validators.NumberRange(min=58, max=67)])
    ecoordinates = FloatField("Itäkoordinaatti: ", [validators.NumberRange(min=16, max=31)])

    class Meta:
        csrf = False