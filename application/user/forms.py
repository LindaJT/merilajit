from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=2)])
    username = StringField("Käyttäjänimi:", [validators.Length(min=2)])
    password = StringField("Salasana:")
 
    class Meta:
        csrf = False