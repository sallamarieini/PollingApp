from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=20)])
    newusername = StringField("Username", [validators.Length(min=3, max=20)])
    newpassword = PasswordField("Password", [validators.Length(min=8, max=20), EqualTo('newpasswordconfirm', message='Passwords must match!')])
    newpasswordconfirm = PasswordField("Repeat password")

    class Meta:
        csrf = False


class EditUsernameForm(FlaskForm):
    username = StringField("New username", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False


class EditPasswordForm(FlaskForm):
    password = PasswordField("New password", [validators.Length(min=8, max=20), EqualTo('passwordconfirm', message='Passwords must match!')])
    passwordconfirm = PasswordField("Repeat new password")

    class Meta:
        csrf = False
