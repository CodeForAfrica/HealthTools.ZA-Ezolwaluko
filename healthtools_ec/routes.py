from flask import redirect, render_template, session, url_for
from flask_mobility.decorators import mobile_template

import healthtools_ec.initiates
import healthtools_ec.locate
import healthtools_ec.reportsurgeons
import healthtools_ec.surgeons  # NOQA
from healthtools_ec.app import app


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
    if session["lang"]:
        return render_template("about/about_xh.html")
    else:
        return render_template("about/about.html")


@app.route("/about-mobi")
def about_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("mobile/about/about_xh.html")
    else:
        return render_template("mobile/about/about.html")


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
    if session["lang"]:
        return render_template("contact/contact_xh.html")
    else:
        return render_template("contact/contact.html")


@app.route("/contact-mobi")
def contact_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("mobile/contact/contact_xh.html")
    else:
        return render_template("mobile/contact/contact.html")


@app.route("/find")
def widgets():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("widgets/widget_searchsurgeon_xh.html")
    else:
        return render_template("widgets/widget_searchsurgeon.html")


@app.route("/find-mobi")
def widgets_mobi():
    if "lang" not in session.keys():
        session["lang"] = 1
        redirect(url_for("home_xh"))
    if session["lang"]:
        return render_template("mobile/widgets/widget_searchsurgeon_xh.html")
    else:
        return render_template("mobile/widgets/widget_searchsurgeon.html")
