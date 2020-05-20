from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField


class PollForm(FlaskForm):
    question = StringField("Poll question")
    description = StringField("Description")
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False
