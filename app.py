from flask_migrate import Migrate

from healthtools_ec.core import app
from healthtools_ec.models import db

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
