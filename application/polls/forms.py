from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField


class PollForm(FlaskForm):
    question = StringField("Poll question", [validators.Length(min=3)])
    description = StringField("Description", [validators.Optional(strip_whitespace=True)])
    option1 = StringField("First answer option", [validators.Length(min=1)])
    option2 = StringField("Second answer option", [validators.Length(min=1)])
    option3 = StringField("Third answer option", [validators.Length(min=1)])
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False
