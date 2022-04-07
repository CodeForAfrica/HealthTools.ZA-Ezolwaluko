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

from .helpers import get_locale_extension
from .models import Surgeon
from .models.surgeons import FindSurgeonForm


@app.route("/locate", methods=["GET", "POST"])
def locator():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = FindSurgeonForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():

            data = int(form.location.data)
            locate = form.location.choices[data][1]
            surgeons = Surgeon.query.filter_by(area=locate).all()
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"find/show{template_locale}.html", surgeons=surgeons
            )
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(render_template(f"find/find{template_locale}.html", form=form))

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )


@app.route("/locator-mobi", methods=["GET", "POST"])
def locator_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = FindSurgeonForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():

            data = int(form.location.data)
            locate = form.location.choices[data][1]
            surgeons = Surgeon.query.filter_by(area=locate).all()
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"mobile/find/show{template_locale}.html", surgeons=surgeons
            )
        else:
            if session["lang"]:
                flash("Please correct the problems below and try again.", "warning")
            else:
                flash("Please correct the problems below and try again.", "warning")
    template_locale = get_locale_extension(session["lang"])
    resp = make_response(
        render_template(f"mobile/find/find{template_locale}.html", form=form)
    )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
