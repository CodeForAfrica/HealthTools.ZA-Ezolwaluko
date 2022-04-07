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

from .helpers import email_report, get_locale_extension
from .models import ReportSurgeon, db
from .models.reportsurgeons import ReportForm


@app.route("/reportsurgeon", methods=["GET", "POST"])
def reports_home():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = ReportForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            report = ReportSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(report)
            db.session.add(report)
            db.session.commit()
            response = email_report(report)
            print(response)
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"reportsurgeons/reportsurgeonredirect{template_locale}.html"
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
        render_template(
            f"reportsurgeons/reportsurgeons{template_locale}.html", form=form
        )
    )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )


@app.route("/reportsurgeon-mobi", methods=["GET", "POST"])
def reports_home_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))

    form = ReportForm(request.form)
    status = 200
    if request.method == "POST":
        if form.validate():
            report = ReportSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(report)
            db.session.add(report)
            db.session.commit()
            response = email_report(report)
            print(response)
            template_locale = get_locale_extension(session["lang"])
            return render_template(
                f"mobile/reportsurgeons/reportsurgeonredirect{template_locale}.html"
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
        render_template(
            f"mobile/reportsurgeons/reportsurgeons{template_locale}.html", form=form
        )
    )

    return (
        resp,
        status,
        # ensure the browser refreshes the page when Back is pressed
        {"Cache-Control": "no-cache, no-store, must-revalidate"},
    )
