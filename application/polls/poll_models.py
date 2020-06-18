from sqlalchemy import text

from application import db


# table for storing information about which polls user has alredy voted on
class UsersAnswered(db.Model):
    __tablename__ = "users_answered"

    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), index=True)

    def __init__(self, poll_id, user_id):
        self.poll_id = poll_id
        self.user_id = user_id


# poll table
class Poll(db.Model):
    __tablename__ = "poll"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False, unique=True, index=True)
    description = db.Column(db.String)
    anonymous = db.Column(db.Boolean, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    polls_answer_options = db.relationship("AnswerOption", backref='poll', lazy=True)
    polls_answer = db.relationship("Answer", backref='poll', lazy=True)
    polls_user_answered = db.relationship("UsersAnswered", backref='poll', lazy=True)

    def __init__(self, question, description, anonymous, creator_id):
        self.question = question
        self.description = description
        self.anonymous = anonymous
        self.creator_id = creator_id

    @staticmethod
    def find_poll_by_question(poll_question):
        stmt = text("SELECT *"
                    " FROM poll"
                    " WHERE poll.question LIKE :poll_question").params(poll_question=poll_question)
        res = db.engine.execute(stmt)

        return res
