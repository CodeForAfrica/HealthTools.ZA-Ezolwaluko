from flask import flash, make_response, render_template, request, session

from healthtools_ec.app import app

from .helpers import email_register, get_locale_extension
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
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"surgeons/registersurgeonredirect{template_locale}.html"
            )
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(
        render_template(f"surgeons/surgeons{template_locale}.html", form=form)
    )

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
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"mobile/surgeons/registersurgeonredirect{template_locale}.html"
            )
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(
        render_template(f"mobile/surgeons/surgeons{template_locale}.html", form=form)
    )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
