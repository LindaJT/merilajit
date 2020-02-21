from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, ValidationError
from application.auth.models import User

def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('That username is taken. Please choose another')


class UserForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=2, max=50)])
    username = StringField("Käyttäjänimi:", [validators.Length(min=2, max=50),validate_username])
    password = StringField("Salasana:", [validators.Length(min=6, max=20)])
    role = SelectField("Käyttäjärooli:", choices=[('ADMIN', 'ADMIN'), 
    ('USER', 'USER')])
 
    class Meta:
        csrf = False

