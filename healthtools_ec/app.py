import os

from flask import Flask

# Mail
from flask_mail import Mail
from flask_mobility import Mobility

# Database
from flask_sqlalchemy import SQLAlchemy

# CSRF protection
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, static_folder="static")
Mobility(app)
env = "local"
app.config["ENV"] = env
app.config.from_pyfile("config.py")

CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://htools:htools@localhost/htools_ezolwaluko"
)
db = SQLAlchemy(app)

mail = Mail(app)
