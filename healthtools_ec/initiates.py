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

from .helpers import email_initiates, get_locale_extension
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
            template_locale = get_locale_extension(session["lang"])
            return render_template(f"initiates/initiateredirect{template_locale}.html")
        else:
            if session["lang"]:
                flash(
                    "Nceda ulungise ezi ngxaki zingezantsi kwaye uzame kwakhona.",
                    "warning",
                )
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(
        render_template(f"initiates/initiates{template_locale}.html", form=form)
    )

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
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"mobile/initiates/initiateredirect{template_locale}.html"
            )
        else:
            if session["lang"]:
                flash(
                    "Nceda ulungise ezi ngxaki zingezantsi kwaye uzame kwakhona.",
                    "warning",
                )
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(
        render_template(f"mobile/initiates/initiates{template_locale}.html", form=form)
    )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
