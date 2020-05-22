from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class NewUserForm(FlaskForm):
    name = StringField("Name")
    newusername = StringField("Username")
    newpassword = PasswordField("Password")

    class Meta:
        csrf = False
