from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms import SelectField

class SpeciesForm(FlaskForm):
    name = StringField("Lajin nimi:", [validators.Length(min=2, max=100)])
    description = StringField("Lajin kuvaus:", [validators.Length(min=2, max=500)])
    category = SelectField("Kategoria:", choices=[('Punalevä', 'Punalevä'), 
    ('Viherlevä', 'Viherlevä'), ('Ruskolevä', 'Ruskolevä'), ('Näkinpartainen', 'Näkinpartainen')])

    class Meta:
        csrf = False