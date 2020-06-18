from sqlalchemy import text

from application import db


# table has answer options for polls
class AnswerOption(db.Model):
    __tablename__ = "answer_option"

    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String, nullable=False)
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