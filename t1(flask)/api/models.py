from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
