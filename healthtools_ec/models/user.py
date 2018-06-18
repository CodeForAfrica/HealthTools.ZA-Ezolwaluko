from ..app import db, app
from ..forms import Form
from flask_mako import render_template

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from flask_security import LoginForm as Form
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, InputRequired


class User(db.Model, UserMixin):
    """
    A user who can login and use Gibela.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), index=True, nullable=False, unique=True)
    password = Column(String(100), default='')
    disabled = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # associations
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "<User phone=%s>" % (self.phone,)

    # Flask-Security requires an active attribute
    @property
    def active(self):
        return not self.disabled

    @active.setter
    def active(self, value):
        self.disabled = not value

    @classmethod
    def create_defaults(self):
        from flask_security.utils import encrypt_password

        admin_user = User()
        admin_user.admin = True
        admin_user.email = "matthew@opendata.durban"
        admin_user.password = encrypt_password('admin')
        return [admin_user]


class Role(db.Model, RoleMixin):
    """
        A user who can login and use Gibela.
    """
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return unicode(self.name)

    @classmethod
    def create_defaults(self):
        return [
            Role(name='admin', description='user can access admin panel'),
        ]


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')))


class LoginForm(Form):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


# user authentication
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form=LoginForm)
app.extensions['security'].render_template = render_template
