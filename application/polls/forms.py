from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class PollForm(FlaskForm):
    question = StringField("Poll question")
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False
