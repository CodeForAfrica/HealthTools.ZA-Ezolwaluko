from healthtools_ec.app import app
from flask import request, url_for, redirect, flash, make_response, session, render_template

from .models import db
from .models import *
from .models.reportsurgeons import ReportForm
from helpers import email_report


@app.route('/reportsurgeon', methods=['GET', 'POST'])
def reports_home():
    if 'lang' not in session.keys():
        session['lang'] = 1
        redirect(url_for('home_xh'))

    form = ReportForm()
    status = 200
    if request.method == 'POST':
        if form.validate():
            report = ReportSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(report)
            db.session.add(report)
            db.session.commit()
            response = email_report(report)
            print(response)
            if session['lang']:
                return render_template('reportsurgeons/reportsurgeonredirect_xh.html')
            else:
                return render_template('reportsurgeons/reportsurgeonredirect.html')
        else:
            if request.is_xhr:
                status = 412
            else:
                if session['lang']:
                    flash('Please correct the problems below and try again.', 'warning')
                else:
                    flash('Please correct the problems below and try again.', 'warning')

    if not request.is_xhr:
        if session['lang']:
            resp = make_response(render_template('reportsurgeons/reportsurgeons_xh.html', form=form))
        else:
            resp = make_response(render_template('reportsurgeons/reportsurgeons.html', form=form))

    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})

@app.route('/reportsurgeon-mobi', methods=['GET', 'POST'])
def reports_home_mobi():
    if 'lang' not in session.keys():
        session['lang'] = 1
        redirect(url_for('home_xh'))

    form = ReportForm()
    status = 200
    if request.method == 'POST':
        if form.validate():
            report = ReportSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(report)
            db.session.add(report)
            db.session.commit()
            response = email_report(report)
            print(response)
            if session['lang']:
                return render_template('mobile/reportsurgeons/reportsurgeonredirect_xh.html')
            else:
                return render_template('mobile/reportsurgeons/reportsurgeonredirect.html')
        else:
            if request.is_xhr:
                status = 412
            else:
                if session['lang']:
                    flash('Please correct the problems below and try again.', 'warning')
                else:
                    flash('Please correct the problems below and try again.', 'warning')

    if not request.is_xhr:
        if session['lang']:
            resp = make_response(render_template('mobile/reportsurgeons/reportsurgeons_xh.html', form=form))
        else:
            resp = make_response(render_template('mobile/reportsurgeons/reportsurgeons.html', form=form))

    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})