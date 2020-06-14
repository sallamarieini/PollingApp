from sqlalchemy import text

from application import db
# moving classes to different files is under consideration

# # table for a many-to-many relationship
# users_answered = db.Table('users_answered',
#                           db.Column('poll_id', db.Integer, db.ForeignKey('poll.id')),
#                           db.Column('user_id', db.Integer, db.ForeignKey('account.id'))
#                           )


# table for storing information about which polls user has alredy voted on
class UsersAnswered(db.Model):
    __tablename__ = "users_answered"

    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, poll_id, user_id):
        self.poll_id = poll_id
        self.user_id = user_id


# poll table
class Poll(db.Model):
    __tablename__ = "poll"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    anonymous = db.Column(db.Boolean, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    polls_answer_options = db.relationship("AnswerOption", backref='poll', lazy=True)
    polls_answer = db.relationship("Answer", backref='poll', lazy=True)
    # polls_user_answered = db.relationship("User", secondary=users_answered,
    #                                       backref=db.backref('answered', lazy='dynamic'))
    polls_user_answered = db.relationship("UsersAnswered", backref='poll', lazy=True)

    def __init__(self, question, description, anonymous, creator_id):
        self.question = question
        self.description = description
        self.anonymous = anonymous
        self.creator_id = creator_id


# table has answer options for polls
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

    @staticmethod
    def get_results(poll_id):
        stmt = text("SELECT answer_option.option, COUNT(answer.answer_option_id) FROM answer_option"
                    " LEFT JOIN answer ON answer.answer_option_id = answer_option.id"
                    " WHERE answer_option.poll_id = :poll_id"
                    " GROUP BY answer_option.id").params(poll_id=poll_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"option": row[0], "count": row[1]})

        return response


# table contains voters voting choices
class Answer(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True)
    answer_option_id = db.Column(db.Integer, db.ForeignKey('answer_option.id'), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, answer_option_id, poll_id):
        self.answer_option_id = answer_option_id
        self.poll_id = poll_id
