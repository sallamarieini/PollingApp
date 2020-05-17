# Importing flask
from flask import Flask
app = Flask(__name__)

# Importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# polls.db is the name of the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///polls.db"
# Asking SQLAlchemy to print all SQL-queries
app.config["SQLALCHEMY_ECHO"] = True

# Creating of db-olio, used for using the database
db = SQLAlchemy(app)

# Importing views
from application import views

# Importing models from polls
from application.polls import models
# Importing views from polls
from application.polls import views

# Creating database tables
db.create_all()
