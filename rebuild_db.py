from healthtools_ec.models import db
from healthtools_ec.models.seeds import seed_db

db.drop_all()
db.create_all()
seed_db(db)
