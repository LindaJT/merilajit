from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=2, max=50)])
    username = StringField("Käyttäjänimi:", [validators.Length(min=2, max=50)])
    password = StringField("Salasana:", [validators.Length(min=6, max=20)])
 
    class Meta:
        csrf = False