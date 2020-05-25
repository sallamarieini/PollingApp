from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField


class PollForm(FlaskForm):
    question = StringField("Poll question", [validators.Length(min=3)])
    description = StringField("Description", [validators.Optional(strip_whitespace=True)])
    option1 = StringField("First answer option")
    option2 = StringField("Second answer option")
    option3 = StringField("Third answer option")
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False
