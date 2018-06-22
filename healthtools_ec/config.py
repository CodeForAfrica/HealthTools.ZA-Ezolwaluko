import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY', 'somethingsupersecret')

MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.sendgrid.net')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_PORT = os.environ.get('MAIL_PORT', 2525)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', False)

MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'ezolwaluko@codeforafrica.org')
MAIL_RECIPIENTS = os.environ.get('MAIL_RECIPIENTS', MAIL_DEFAULT_SENDER).split(',')

# Flask-Security config
SECURITY_URL_PREFIX = "/user"
SECURITY_PASSWORD_HASH = "sha256_crypt"
SECURITY_PASSWORD_SALT = "sha256_crypt"
# SECURITY_USER_IDENTITY_ATTRIBUTES = 'name'

# Flask-Security admin
# SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_CHANGE_URL = "/change-password/"
SECURITY_RESET_URL = "/forgot-password"

# Flask-Security email subject lines
SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to Ezolwaluko"
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = "Password reset instructions for your Ezolwaluko account"

# Flask-Security features
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
