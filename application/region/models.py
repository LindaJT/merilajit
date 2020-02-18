from application import db

regionspecies = db.Table('regionspecies',
    db.Column('region_id', db.Integer, db.ForeignKey('region.id'), primary_key=True),
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'), primary_key=True)
)

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))

    regionspecies = db.relationship("Species", secondary=regionspecies, lazy='subquery', backref=db.backref('regions', lazy=True))

    def __init__(self, name):
        self.name = name
