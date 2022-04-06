from flask import flash, make_response, render_template, request, session

from healthtools_ec.app import app

from .helpers import email_register
from .models import RegisterSurgeon, db
from .models.surgeons import RegisterForm


@app.route("/register", methods=["GET", "POST"])
def surgeons_register():
    form = RegisterForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            surgeon = RegisterSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(surgeon)
            db.session.add(surgeon)
            db.session.commit()
            response = email_register(surgeon)
            print(response)
            if session["lang"]:
                return render_template("surgeons/registersurgeonredirect_xh.html")
            else:
                return render_template("surgeons/registersurgeonredirect.html")
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")

    if session["lang"]:
        resp = make_response(render_template("surgeons/surgeons_xh.html", form=form))
    else:
        resp = make_response(render_template("surgeons/surgeons.html", form=form))

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )


@app.route("/register-mobi", methods=["GET", "POST"])
def surgeons_register_mobi():
    form = RegisterForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            surgeon = RegisterSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(surgeon)
            db.session.add(surgeon)
            db.session.commit()
            response = email_register(surgeon)
            print(response)
            if session["lang"]:
                return render_template(
                    "mobile/surgeons/registersurgeonredirect_xh.html"
                )
            else:
                return render_template("mobile/surgeons/registersurgeonredirect.html")
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")

    if session["lang"]:
        resp = make_response(
            render_template("mobile/surgeons/surgeons_xh.html", form=form)
        )
    else:
        resp = make_response(
            render_template("mobile/surgeons/surgeons.html", form=form)
        )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
