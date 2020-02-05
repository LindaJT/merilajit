from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, FloatField
from wtforms import SelectField

class ObsForm(FlaskForm):
    description = StringField("Havainnon kuvaus: ")
    date = DateField("Havainnon päivämäärä: ")
    ncoordinates = FloatField("Pohjoiskoordinaatti:")
    ecoordinates = FloatField("Itäkoordinaatti: ")

    class Meta:
        csrf = False