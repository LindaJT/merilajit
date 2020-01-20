from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    category = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name