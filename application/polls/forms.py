from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class PollForm(FlaskForm):
    question = StringField("Poll question", [validators.Length(min=3)])
    description = StringField("Description", [validators.Optional(strip_whitespace=True)])
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False
