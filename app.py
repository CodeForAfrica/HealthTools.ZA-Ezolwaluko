from flask_migrate import Migrate

from healthtools_ec.core import app
from healthtools_ec.models import db

migrate = Migrate(app, db)
