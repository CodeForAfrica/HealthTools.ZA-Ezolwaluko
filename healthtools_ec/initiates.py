from flask import (
    flash,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from healthtools_ec.app import app

from .helpers import email_initiates
from .models import Initiate, db
from .models.initiates import InitiateForm


@app.route("/initiates", methods=["GET", "POST"])
def initiates_home():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = InitiateForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            initiate = Initiate()
            with db.session.no_autoflush:
                form.populate_obj(initiate)
            db.session.add(initiate)
            db.session.commit()
            response = email_initiates(initiate)
            print(response)
            if session["lang"]:
                return render_template("initiates/initiateredirect_xh.html")
            else:
                return render_template("initiates/initiateredirect.html")
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")
    if session["lang"]:
        resp = make_response(render_template("initiates/initiates_xh.html", form=form))
    else:
        resp = make_response(render_template("initiates/initiates.html", form=form))

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )


@app.route("/initiates-mobi", methods=["GET", "POST"])
def initiates_home_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = InitiateForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            initiate = Initiate()
            with db.session.no_autoflush:
                form.populate_obj(initiate)
            db.session.add(initiate)
            db.session.commit()
            response = email_initiates(initiate)
            print(response)
            if session["lang"]:
                return render_template("mobile/initiates/initiateredirect_xh.html")
            else:
                return render_template("mobile/initiates/initiateredirect.html")
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")

    if session["lang"]:
        resp = make_response(
            render_template("mobile/initiates/initiates_xh.html", form=form)
        )
    else:
        resp = make_response(
            render_template("mobile/initiates/initiates.html", form=form)
        )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
