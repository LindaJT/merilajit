from application import db
from sqlalchemy.sql import text

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    category = db.Column(db.String(50))

    observations = db.relationship("Observation", backref='species', cascade="all, delete, delete-orphan")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def count_observations_by_species():
        stmt = text("SELECT Species.id, Species.name, COUNT(Observation.id) FROM Species"
                    " LEFT JOIN Observation ON Observation.species_id = Species.id"
                    " GROUP BY Species.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "count":row[2]})

        return response