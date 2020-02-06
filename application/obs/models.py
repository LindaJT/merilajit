from application import db
from datetime import date

class Observation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    date = db.Column(db.Date)
    ncoordinates = db.Column(db.Float())
    ecoordinates = db.Column(db.Float())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable =False)

    def __init__(self, description):
        self.description = description