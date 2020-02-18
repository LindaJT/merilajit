from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms import SelectField

class RegionForm(FlaskForm):
    name = StringField("Alue:", [validators.Length(min=2, max=100)])
    description = StringField("Alueen kuvaus:", [validators.Length(min=2, max=500)]) 
 
    class Meta:
        csrf = False