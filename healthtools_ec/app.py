import os
from flask import Flask
from flask_mobility import Mobility


app = Flask(__name__, static_folder='static')
Mobility(app)
env = 'local'
app.config['ENV'] = env
app.config.from_pyfile('config.py')

# CSRF protection
from flask_wtf.csrf import CsrfProtect

CsrfProtect(app)

# Database
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql://htools:htools@localhost/htools_ezolwaluko')
db = SQLAlchemy(app)

# Mail
from flask_mail import Mail

mail = Mail(app)
