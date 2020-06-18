from sqlalchemy import text

from application import db


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, index=True, unique=True)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    users_polls = db.relationship("Poll", backref='account', lazy=True)
    users_user_answered = db.relationship("UsersAnswered", backref='account', lazy=True)

    def __init__(self, name, username, password, admin):
        self.name = name
        self.username = username
        self.password = password
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated():
        return True

    def roles(self):
        if self.admin:
            return ["ADMIN"]
        else:
            return ["ANY"]

    @staticmethod
    def get_voting_activity():
        stmt = text("SELECT account.username, COUNT(users_answered.user_id)"
                    " FROM account"
                    " LEFT JOIN users_answered ON users_answered.user_id = account.id"
                    " GROUP BY account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username": row[0], "count": row[1]})

        return response
