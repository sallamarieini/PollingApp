from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, BooleanField


# not yet sure what i'm going to do with the description field so the validators are a little odd
class PollForm(FlaskForm):
    question = StringField("Poll question", [validators.Length(min=3, max=150)])
    description = StringField("Description", [validators.Optional(strip_whitespace=True), validators.length(min=3, max=150)])
    option1 = StringField("First answer option", [validators.Length(min=1, max=80)])
    option2 = StringField("Second answer option", [validators.Length(min=1, max=80)])
    option3 = StringField("Third answer option", [validators.Length(min=1, max=80)])
    anonymous = BooleanField("Anonymous poll")
    submit = SubmitField("Submit")

    class Meta:
        csrf = False


class EditPollForm(FlaskForm):
    question = StringField("Poll question")

    class Meta:
        csrf = False


class SearchForm(FlaskForm):
    question = StringField("Search by question", [validators.Length(min=1, max=150)])

    class Meta:
        csrf = False
