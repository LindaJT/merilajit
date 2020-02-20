from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

class UserForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=2, max=50)])
    username = StringField("Käyttäjänimi:", [validators.Length(min=2, max=50)])
    password = StringField("Salasana:", [validators.Length(min=6, max=20)])
    role = SelectField("Käyttäjärooli:", choices=[('ADMIN', 'ADMIN'), 
    ('USER', 'USER')])
 
    class Meta:
        csrf = False