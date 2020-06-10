# Importing flask
from flask import Flask
# importing bcrypt
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///polls.db"
    app.config["SQLALCHEMY_ECHO"] = True

# Creating of db-olio, used for using the database
db = SQLAlchemy(app)

# login
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps


def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# Importing views
from application import views

# Importing models from polls
from application.polls import models
# Importing views from polls
from application.polls import views

# Importing models from auth
from application.auth import models
from application.auth import views

app.static_folder = "static"

# login functionality
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Creating database tables
db.create_all()
