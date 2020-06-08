from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.polls.models import Poll, AnswerOption, Answer, UsersAnswered
from application.polls.forms import PollForm, EditPollForm
from application.auth.models import User


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

    pquestion = request.form.get("question")
    p = Poll(request.form.get("question"), request.form.get("description"), form.anonymous.data,
             current_user.id)

    db.session().add(p)
    db.session().commit()

    p_id = Poll.query.filter_by(question=pquestion).first()

    o1 = AnswerOption(request.form.get("option1"), p_id.id)
    o2 = AnswerOption(request.form.get("option2"), p_id.id)
    o3 = AnswerOption(request.form.get("option3"), p_id.id)

    db.session().add(o1)
    db.session().add(o2)
    db.session().add(o3)
    db.session().commit()

    return redirect(url_for("polls_index"))


@app.route("/polls/edit/<poll_id>/", methods=["POST", "GET"])
@login_required
def polls_edit(poll_id):
    poll = Poll.query.get(poll_id)

    options = AnswerOption.query.filter_by(poll_id=poll.id)
    option1 = options[0].option
    option2 = options[1].option
    option3 = options[2].option

    form = PollForm(request.form)

    if poll.creator_id != current_user.id:
        # this needs a page to inform about an error
        return

    if request.method == "POST":
        if not form.validate():
            return render_template("polls/edit_poll.html", poll=poll, form=form, option1=option1, option2=option2,
                                   option3=option3)

        updated_question = request.form.get("question")
        updated_description = request.form.get("description")
        option1 = request.form.get("option1")
        option2 = request.form.get("option2")
        option3 = request.form.get("option3")

        poll.question = updated_question
        poll.description = updated_description

        answer_options = AnswerOption.query.filter_by(poll_id=poll.id)
        answer_options[0].option = option1
        answer_options[1].option = option2
        answer_options[2].option = option3

        db.session.commit()

        new_options = [option1, option2, option3]

        # return redirect(url_for("polls_index"))
        return render_template("polls/single_poll.html", poll=poll, optionlist=new_options)

    return render_template("polls/edit_poll.html", poll=poll, form=PollForm(), option1=option1, option2=option2,
                           option3=option3)


@app.route("/polls/<poll_id>", methods=["POST", "GET"])
def single_poll(poll_id):
    if request.method == "POST":
        poll = Poll.query.get(poll_id)

        vote = request.form['options']
        # v = Answer()
        answer_option_id = AnswerOption.query.filter_by(poll_id=poll_id, option=vote).first().id

        answer = Answer(answer_option_id, poll_id)
        # current_user.answered.append(poll)
        user_answered = UsersAnswered(poll.id, current_user.id)

        db.session().add(answer)
        db.session().add(user_answered)
        db.session().commit()

        return render_template("polls/thankyou.html", poll=poll)

    poll = Poll.query.get(poll_id)
    options = AnswerOption.query.filter_by(poll_id=poll_id)

    optionlist = []
    for o in options:
        optionlist.append(o.option)

    # voting only once while logged in does NOT work
    # now a poll can only be voted once if any logged in user votes on it (other users can't vote)
    already_answered_list = UsersAnswered.query.filter_by(poll_id=poll_id).first()

    if not already_answered_list:
        return render_template("polls/single_poll.html", poll=poll, optionlist=optionlist, error=None)

    return render_template("polls/single_poll.html", poll=poll, optionlist=optionlist,
                           error="lol")


@app.route("/polls/delete/<poll_id>", methods=["POST"])
@login_required
def delete_poll(poll_id):
    Answer.query.filter_by(poll_id=poll_id).delete()
    AnswerOption.query.filter_by(poll_id=poll_id).delete()
    UsersAnswered.query.filter_by(poll_id=poll_id).delete()
    Poll.query.filter_by(id=poll_id).delete()
    db.session.commit()

    return redirect(url_for("polls_index"))


@app.route("/polls/results/<poll_id>")
@login_required
def show_results(poll_id):
    poll = Poll.query.get(poll_id)

    return render_template("polls/results.html", results=AnswerOption.get_results(poll_id=poll_id), poll=poll)
