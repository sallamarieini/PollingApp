from application import db


class Poll(db.Model):
    __tablename__ = "poll"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    creator_id = db.Column(db.Integer)

    polls = db.relationship("AnswerOption", backref='poll', lazy=True)
    polls2 = db.relationship("Answer", backref='poll', lazy=True)

    def __init__(self, question, description, creator_id):
        self.question = question
        self.description = description
        self.creator_id = creator_id


class AnswerOption(db.Model):
    __tablename__ = "answer_option"

    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)

    answer_options = db.relationship("Answer", backref='answer_option', lazy=True)

    def __init__(self, option, poll_id):
        self.option = option
        self.poll_id = poll_id


class Answer(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True)
    answer_option_id = db.Column(db.Integer, db.ForeignKey('answer_option.id'), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, answer_option_id, poll_id):
        self.answer_option_id = answer_option_id
        self.poll_id = poll_id
