from . import *  # noqa
from ..app import app
import pandas as pd
import math
import os

def seed_db(db):
    """ Add seed entities to the database. """
    with app.app_context():
        for x in User.create_defaults():
            db.session.add(x)
        db.session.commit()

        df = pd.read_csv('C:/Users/Wasim/Documents/GitHub/healthtools-citypress/healthtools_ec/data/traditional.csv')
        for i in range(0, len(df)):
            surgeon = Surgeon()
            surgeon.name = df.iloc[i][0]
            if math.isnan(df.iloc[i][1]):
                surgeon.id_number = None
            else:
                surgeon.id_number = str(int(df.iloc[i][1]))
            if isinstance(df.iloc[i][2], str):
                surgeon.area = df.iloc[i][2]
            else:
                if math.isnan(df.iloc[i][2]):
                    surgeon.area = None
                else:
                    surgeon.area = df.iloc[i][2]
            if math.isnan(df.iloc[i][3]):
                surgeon.phone_number = None
            else:
                surgeon.phone_number = '0' + str(int(df.iloc[i][3]))

            if isinstance(df.iloc[i][4], str):
                surgeon.standard = df.iloc[i][4]
            else:
                if math.isnan(df.iloc[i][4]):
                    surgeon.standard = None
                else:
                    surgeon.standard = df.iloc[i][4]

            if isinstance(df.iloc[i][5], str):
                surgeon.category = df.iloc[i][5]
            else:
                if math.isnan(df.iloc[i][5]):
                    surgeon.category = None
                else:
                    surgeon.category = df.iloc[i][5]
            db.session.add(surgeon)
        db.session.commit()
