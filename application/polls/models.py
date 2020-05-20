from application import db


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    creator_id = db.Column(db.Integer)

    def __init__(self, question, description):
        self.question = question
        self.description = description
