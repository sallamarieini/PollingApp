from application import app, db, login_required, PER_PAGE
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application.polls.poll_models import Poll, UsersAnswered
from application.polls.answer_models import AnswerOption, Answer
from application.polls.forms import PollForm, SearchForm


@app.route("/")
def frontpage():
    return render_template("index.html")


@app.route("/polls", methods=["GET"])
def polls_index():
    page = request.args.get('page', 1, type=int)
    polls = Poll.query.paginate(page, PER_PAGE, False)

    next_url = url_for('polls_index', page=polls.next_num) \
        if polls.has_next else None
    prev_url = url_for('polls_index', page=polls.prev_num) \
        if polls.has_prev else None

    if len(polls.items) == 0:
        return render_template("polls/list.html", message="There seems to be no polls. Please create a poll.",
                               word=None)

    return render_template("polls/list.html", polls=polls.items, word=None, next_url=next_url, prev_url=prev_url)


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
    poll = Poll.query.filter_by(question=pquestion).first()

    if poll:
        return render_template("polls/new.html", form=form, message="There is a poll with this question already."
                                                                    " Please choose another question.")

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
        # show error page
        return render_template("no_access.html")

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

        return render_template("polls/single_poll.html", poll=poll, optionlist=new_options)

    return render_template("polls/edit_poll.html", poll=poll, form=PollForm(), option1=option1, option2=option2,
                           option3=option3)


@app.route("/polls/<poll_id>", methods=["POST", "GET"])
def single_poll(poll_id):
    if request.method == "POST":
        poll = Poll.query.get(poll_id)

        vote = request.form['options']

        answer_option_id = AnswerOption.query.filter_by(poll_id=poll_id, option=vote).first().id

        answer = Answer(answer_option_id, poll_id)

        if current_user.is_authenticated and poll.anonymous == 0:
            user_answered = UsersAnswered(poll.id, current_user.id)
            db.session().add(user_answered)

        db.session().add(answer)
        db.session().commit()

        return render_template("polls/thankyou.html", poll=poll)

    poll = Poll.query.get(poll_id)
    options = AnswerOption.query.filter_by(poll_id=poll_id)

    optionlist = []
    for o in options:
        optionlist.append(o.option)

    if current_user.is_authenticated:
        condition = UsersAnswered.query.filter_by(user_id=current_user.id, poll_id=poll.id).first()
        if not condition:
            return render_template("polls/single_poll.html", poll=poll, optionlist=optionlist, error=None)

    return render_template("polls/single_poll.html", poll=poll, optionlist=optionlist,
                           error="You have already voted on this poll!")


@app.route("/polls/delete/<poll_id>", methods=["POST", "GET"])
@login_required
def delete_poll(poll_id):
    poll = Poll.query.get(poll_id)

    if int(current_user.id) == int(poll.creator_id) or current_user.admin:
        Answer.query.filter_by(poll_id=poll_id).delete()
        AnswerOption.query.filter_by(poll_id=poll_id).delete()
        UsersAnswered.query.filter_by(poll_id=poll_id).delete()
        Poll.query.filter_by(id=poll_id).delete()
        db.session.commit()
    else:
        return render_template("no_access.html")

    return redirect(url_for("polls_index"))


@app.route("/polls/results/<poll_id>")
@login_required
def show_results(poll_id):
    poll = Poll.query.get(poll_id)

    if poll.creator_id != current_user.id:
        # show error page
        return render_template("no_access.html")

    return render_template("polls/results.html", results=AnswerOption.get_results(poll_id=poll_id), poll=poll)


@app.route("/polls/search")
def polls_search():
    return render_template("polls/search.html", form=SearchForm())


@app.route("/polls/search_results", methods=["POST", "GET"])
def polls_search_results():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template("polls/search.html", form=form)

    search_word = request.form.get("question")

    results = Poll.find_poll_by_question("%" + search_word + "%")

    helper = []
    for r in results:
        helper.append(r)

    if not helper:
        return render_template("polls/search.html", form=form, message="No results were found.")

    return render_template("polls/list.html", polls=helper, word=search_word)
