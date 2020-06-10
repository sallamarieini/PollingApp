from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # validations

    user = User.query.filter_by(username=form.username.data).first()

    if not user:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    candidate = form.password.data

    if not bcrypt.check_password_hash(user.password, candidate):
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new")
def auth_form():
    return render_template("auth/registerform.html", form=NewUserForm())


@app.route("/auth/", methods=["POST"])
def create_new_user():
    form = NewUserForm(request.form)

    user = User.query.filter_by(username=form.newusername.data).first()
    if user:
        return render_template("auth/registerform.html", form=form, error="This username is already taken!")

    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    all_users = User.query.all()
    user_count = len(all_users)

    admin = False

    if user_count == 0:
        admin = True

    pw_hash = bcrypt.generate_password_hash(form.newpassword.data).decode('utf-8')

    u = User(form.name.data, form.newusername.data, pw_hash, admin)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))
