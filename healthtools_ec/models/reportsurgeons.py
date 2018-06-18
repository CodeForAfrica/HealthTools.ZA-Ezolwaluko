from ..app import db
from ..forms import Form
from wtforms import StringField, validators
from sqlalchemy import func
from wtforms.widgets import TextArea


class ReportSurgeon(db.Model):
    __tablename__ = 'reportsurgeons'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    opt_name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(10))
    surgeons_name = db.Column(db.String(50))
    area = db.Column(db.String(255))
    report_problem = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, unique=False, nullable=False,
                          server_default=func.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class ReportForm(Form):
    class Meta:
        model = ReportSurgeon

    opt_name = StringField('Name of person reporting', [validators.Length(max=50), validators.Optional()])
    phone_number = StringField('Phone Number', [validators.Length(min=10, max=10), validators.DataRequired()])
    surgeons_name = StringField('Surgeon Name', [validators.Length(max=50), validators.DataRequired()])
    area = StringField('Area of the problem', [validators.Length(max=255), validators.DataRequired()])
    report_problem = StringField('Description of problem', [validators.Length(max=1024), validators.DataRequired()],
                                 widget=TextArea())

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

    def validate(self):
        return super(ReportForm, self).validate()

    def populate_obj(self, obj):
        super(ReportForm, self).populate_obj(obj)
