from ..app import db
from ..forms import Form
from wtforms import StringField, validators, SelectField
from healthtools_ec.app import db
from sqlalchemy import func


class Surgeon(db.Model):
    __tablename__ = 'surgeons'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    id_number = db.Column(db.String(50), nullable=True)
    area = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(10), nullable=True)
    standard = db.Column(db.String(10), nullable=True)
    category = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RegisterSurgeon(db.Model):
    __tablename__ = 'register_surgeons'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    area = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(10), nullable=True)
    timestamp = db.Column(db.DateTime(timezone=True), index=True, unique=False, nullable=False,
                          server_default=func.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RegisterForm(Form):
    class Meta:
        model = RegisterSurgeon
    name = StringField('Initiate Name', [validators.Length(max=50), validators.DataRequired()])
    phone_number = StringField('Phone Number', [validators.Length(min=10, max=10), validators.DataRequired()])
    area = StringField('Area where you work in', [validators.Length(max=255), validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate(self):
        return super(RegisterForm, self).validate()

    def populate_obj(self, obj):
        super(RegisterForm, self).populate_obj(obj)


class FindSurgeonForm(Form):

    location = SelectField('Select your area')

    def __init__(self, *args, **kwargs):
        super(FindSurgeonForm, self).__init__(*args, **kwargs)
        query = Surgeon.query.distinct(Surgeon.area)
        self.location.choices = [[str(i), row.area] for i, row in enumerate(query.all())]

    def validate(self):
        return super(FindSurgeonForm, self).validate()

