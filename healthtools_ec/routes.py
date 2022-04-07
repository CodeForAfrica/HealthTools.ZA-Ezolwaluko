from flask import redirect, render_template, session, url_for
from flask_mobility.decorators import mobile_template

import healthtools_ec.initiates
import healthtools_ec.locate
import healthtools_ec.reportsurgeons
import healthtools_ec.surgeons  # NOQA
from healthtools_ec.app import app
from healthtools_ec.helpers import get_locale_extension


@app.route("/")
def home():
    if "lang" in session.keys():
        if session["lang"]:
            return redirect(url_for("home_xh"))
        else:
            return redirect(url_for("home_en"))
    session["lang"] = 1
    return redirect(url_for("home_xh"))


@app.route("/xh")
@mobile_template("/{mobile/}home/home_xh.html")
def home_xh(template):
    session["lang"] = 1
    return render_template(template)


@app.route("/en")
@mobile_template("/{mobile/}home/home.html")
def home_en(template):
    session["lang"] = 0
    return render_template(template)


@app.route("/about")
def about():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"about/about{template_locale}.html")


@app.route("/about-mobi")
def about_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"mobile/about/about{template_locale}.html")


@app.route("/faq")
def faq():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("faq/faq.html")
    else:
        return render_template("faq/faq.html")


@app.route("/faq-mobi")
def faq_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("mobile/faq/faq.html")
    else:
        return render_template("mobile/faq/faq.html")


@app.route("/contact")
def contact():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"contact/contact{template_locale}.html")


@app.route("/contact-mobi")
def contact_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"mobile/contact/contact{template_locale}.html")


@app.route("/find")
def widgets():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"widgets/widget_searchsurgeon{template_locale}.html")


@app.route("/find-mobi")
def widgets_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    template_locale = get_locale_extension(session["lang"])
    return render_template(f"mobile/widgets/widget_searchsurgeon{template_locale}.html")
