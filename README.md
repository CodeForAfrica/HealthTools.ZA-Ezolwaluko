# Healthtools-Ezolwaluko - Flask
Healthtools-Ezolwaluko Repo

## Readme Contents
- [Project Documentation Links](/README.md#project-documentation-links)
- [Dev Environments](/README.md#dev-environments)
- [Techinical Specifications](/README.md#technical-specifications)
- [Module List and Syntax](/README.md#module-list-and-syntax)
- [Caveats, Dev Notes and or Outstanding Bugs](/README.md#caveats-dev-notes-and-or-outstanding-bugs)

## Project Documentation Links


## Dev Environments
#### Staging Environment
- Local Environment
#### Live Environment
- Standard Heroku App
## Technical Specs
- Python Flask
- Bootstrap 3

#### Device and Browser Information
V1.0 will be a mobile first web-app, designed purely for mobile but viewable by web.
The following browsers and devices need to be 100% design match:
- Latest 3 Chrome, IE, Edge, Firefox Desktop
- Latest 2 Chrome, Edge, Safari Mobile
V2.0 will include a desktop design.

## Module list and syntax
#### How to set up for Development ####
* clone the repo
* install a virtual env and activate it: `virtualenv --no-site-packages env; source env/bin/activate`
* install requirements: `pip install -r requirements.txt`

#### How To Set Up the Database
Setup the PostgreSQL database (minimum version 9.6.*)
```
psql -U postgres
=# CREATE USER healthtools WITH PASSWORD 'healthtools';
=# CREATE DATABASE healthtools;
=# GRANT ALL PRIVILEGES ON DATABASE healthtools TO healthtools;
=# \q
```
Construct your db app-side:
```
from healthtools_ec.models import db
from healthtools_ec.models.seeds import seed_db
run 'python rebuild_db.py'
```

#### Deploying database changes ####
* Healthtools-Ezolwaluko App uses Flask-Migrate (which uses Alembic) to handle database migrations.
* To add a new model or make changes, update the SQLAlchemy definitions in `healthtools_ec/models/`. Then run
`python app.py db migrate --message "a description of your change"`
* This will autogenerate a change. Double check that it make sense. To apply it on your machine, run
`python app.py db upgrade head`
