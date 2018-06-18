from ..app import db
from ..forms import Form
from wtforms import StringField, validators
from sqlalchemy import func
from wtforms.widgets import TextArea


class Initiate(db.Model):
    __tablename__ = 'initiates'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    initiate_problem = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, unique=False, nullable=False,
                          server_default=func.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class InitiateForm(Form):
    class Meta:
        model = Initiate

    name = StringField('Initiate Name', [validators.Length(max=50), validators.DataRequired()])
    phone_number = StringField('Phone Number', [validators.Length(min=10, max=10), validators.DataRequired()])
    initiate_problem = StringField('Initiate Problem Description', [validators.Length(max=1024),
                                                                    validators.DataRequired()], widget=TextArea())

    def __init__(self, *args, **kwargs):
        super(InitiateForm, self).__init__(*args, **kwargs)

    def validate(self):
        return super(InitiateForm, self).validate()

    def populate_obj(self, obj):
        super(InitiateForm, self).populate_obj(obj)
