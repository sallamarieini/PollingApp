from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from application import app, db, bcrypt, login_required, PER_PAGE
from application.auth.models import User
from application.polls.models import Poll, Answer, AnswerOption, UsersAnswered
from application.auth.forms import LoginForm, NewUserForm, EditUsernameForm, EditPasswordForm


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
def auth_create_new_user():
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

    return render_template("index.html", message="Account created successfully.")


@app.route("/auth/list_users")
@login_required(role="ADMIN")
def auth_list():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page, PER_PAGE, False)
    # users = User.query.all()

    next_url = url_for('auth_list', page=users.next_num) \
        if users.has_next else None
    prev_url = url_for('auth_list', page=users.prev_num) \
        if users.has_prev else None

    return render_template("auth/list.html", users=users.items, next_url=next_url, prev_url=prev_url)


@app.route("/auth/delete/<user_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def auth_delete(user_id):
    # find all polls created by the user
    polls = Poll.query.filter_by(creator_id=user_id).all()

    # delete everything that has something to do with polls the user has created
    for poll in polls:
        Answer.query.filter_by(poll_id=poll.id).delete()
        AnswerOption.query.filter_by(poll_id=poll.id).delete()
        UsersAnswered.query.filter_by(poll_id=poll.id).delete()

    # delete all mentions of user from table users_answered
    UsersAnswered.query.filter_by(user_id=user_id).delete()
    # delete poll
    Poll.query.filter_by(creator_id=user_id).delete()
    # delete user
    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return redirect(url_for("auth_list"))


@app.route("/auth/profile")
@login_required
def auth_profile():
    return render_template("auth/profile.html")


@app.route("/auth/edit/username/<user_id>", methods=["POST", "GET"])
@login_required
def auth_edit_username(user_id):
    user = User.query.get(user_id)

    form = EditUsernameForm(request.form)

    if current_user.id != int(user_id):
        # display error page
        return render_template("no_access.html")

    if request.method == "POST":

        if not form.validate():
            return render_template("auth/edit_username.html", user=user, form=form)

        updated_username = request.form.get("username")

        user_check = User.query.filter_by(username=form.username.data).first()
        if user_check:
            return render_template("auth/edit_username.html", user=user, form=form,
                                   error="This username is already taken!")

        user.username = updated_username

        db.session.commit()

        return render_template("auth/profile.html")

    return render_template("auth/edit_username.html", user=user, form=EditUsernameForm())


@app.route("/auth/edit/password/<user_id>", methods=["POST", "GET"])
@login_required
def auth_edit_password(user_id):
    user = User.query.get(user_id)

    form = EditPasswordForm(request.form)

    if current_user.id != int(user_id) or current_user.is_authenticated is False:
        # display error page
        return render_template("no_access.html")

    if request.method == "POST":

        if not form.validate():
            return render_template("auth/edit_password.html", user=user, form=form)

        updated_password = request.form.get("password")

        # if len(updated_password) != 0:
        pw_hash = bcrypt.generate_password_hash(updated_password).decode('utf-8')
        user.password = pw_hash

        db.session.commit()

        return render_template("auth/profile.html", message="Password changed. You can now use your new password.")

    return render_template("auth/edit_password.html", user=user, form=EditPasswordForm())


@app.route("/auth/user_activity")
@login_required(role="ADMIN")
def auth_user_activity():
    results = User.get_voting_activity()

    return render_template("auth/user_activity.html", results=results)
