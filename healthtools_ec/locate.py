from healthtools_ec.app import app
from flask import request, url_for, redirect, flash, make_response, session, render_template
from .models import Surgeon
from .models.surgeons import FindSurgeonForm

@app.route('/locate', methods=['GET', 'POST'])
def locator():
    if 'lang' not in session.keys():
        session['lang'] = 1
        redirect(url_for('home_xh'))

    form = FindSurgeonForm(request.form)
    status = 200
    if request.method == 'POST':
        if form.validate():

            data = int(form.location.data)
            locate = form.location.choices[data][1]
            surgeons = Surgeon.query.filter_by(area=locate).all()


            if session['lang']:
                return render_template('find/show_xh.html', surgeons=surgeons)
            else:

                return render_template('find/show.html', surgeons=surgeons)
        else:
            if session['lang']:
                flash('Please correct the problems below and try again.', 'warning')
            else:
                flash('Please correct the problems below and try again.', 'warning')

    if session['lang']:
        resp = make_response(render_template('find/find_xh.html', form=form))
    else:
        resp = make_response(render_template('find/find.html', form=form))

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})

@app.route('/locator-mobi', methods=['GET', 'POST'])
def locator_mobi():
    if 'lang' not in session.keys():
        session['lang'] = 1
        redirect(url_for('home_xh'))

    form = FindSurgeonForm(request.form)
    status = 200
    if request.method == 'POST':
        if form.validate():

            data = int(form.location.data)
            locate = form.location.choices[data][1]
            surgeons = Surgeon.query.filter_by(area=locate).all()


            if session['lang']:
                return render_template('mobile/find/show_xh.html', surgeons=surgeons)
            else:
                return render_template('mobile/find/show.html', surgeons=surgeons)
        else:
            if session['lang']:
                flash('Please correct the problems below and try again.', 'warning')
            else:
                flash('Please correct the problems below and try again.', 'warning')

    if session['lang']:
        resp = make_response(render_template('mobile/find/find_xh.html', form=form))
    else:
        resp = make_response(render_template('mobile/find/find.html', form=form))

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})
