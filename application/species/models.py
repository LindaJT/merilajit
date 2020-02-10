from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    category = db.Column(db.String(50))

    observations = db.relationship("Observation", backref='species', cascade="all, delete, delete-orphan")

    def __init__(self, name):
        self.name = name