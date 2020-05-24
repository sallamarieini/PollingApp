from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.polls.models import Poll
from application.polls.forms import PollForm, EditPollForm


@app.route("/")
def frontpage():
    return render_template("index.html")


@app.route("/polls", methods=["GET"])
def polls_index():
    return render_template("polls/list.html", polls=Poll.query.all())


@app.route("/polls/new")
@login_required
def newpolls_form():
    return render_template("polls/new.html", form=PollForm())


@app.route("/polls/", methods=["POST"])
@login_required
def polls_create():
    form = PollForm(request.form)

    if not form.validate():
        return render_template("polls/new.html", form=form)

    p = Poll(request.form.get("question"), request.form.get("description"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("polls_index"))


@app.route("/polls/edit/<poll_id>/", methods=["POST", "GET"])
@login_required
def polls_edit(poll_id):
    poll = Poll.query.get(poll_id)

    if request.method == "POST":
        updated_question = request.form.get("question")
        updated_description = request.form.get("description")
        poll.question = updated_question
        poll.description = updated_description
        db.session.commit()
        # return redirect(url_for("polls_index"))
        return render_template("polls/single_poll.html", poll=poll)

    return render_template("polls/edit_poll.html", poll=poll, form=PollForm())


@app.route("/polls/<poll_id>")
def single_poll(poll_id):
    poll = Poll.query.get(poll_id)
    return render_template("polls/single_poll.html", poll=poll)


@app.route("/polls/delete/<poll_id>", methods=["POST"])
@login_required
def delete_poll(poll_id):
    Poll.query.filter_by(id=poll_id).delete()
    db.session.commit()

    return redirect(url_for("polls_index"))
