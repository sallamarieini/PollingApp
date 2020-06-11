from application import db


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
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
