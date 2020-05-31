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

# Importing views
from application import views

# Importing models from polls
from application.polls import models
# Importing views from polls
from application.polls import views

# Importing models from auth
from application.auth import models
from application.auth import views

# login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

app.static_folder = "static"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Creating database tables
db.create_all()
