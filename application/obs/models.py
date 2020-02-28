from application import db
from datetime import date
from sqlalchemy.sql import text

class Observation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    date = db.Column(db.Date)
    ncoordinates = db.Column(db.Float())
    ecoordinates = db.Column(db.Float())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable =False)

    def __init__(self, description):
        self.description = description

    @staticmethod
    def observations_by_user(user_id):
        stmt = text("SELECT Species.name, Observation.description, Observation.date, Observation.ncoordinates, Observation.ecoordinates, Observation.id  FROM Species "
                    "INNER JOIN Observation ON Observation.species_id = Species.id "
                    "INNER JOIN Account ON Observation.account_id = Account.id "
                    " WHERE Account.id = :x")
        res = db.engine.execute(stmt, x=user_id)

        response = []
        for row in res:
            response.append({"name":row[0], "description":row[1], "date":row[2], "ncoordinates":row[3], "ecoordinates":row[4], "id":row[5]})

        return response