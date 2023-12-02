from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flat(db.Model):
    __tablename__ = "flats"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=False, nullable=False)
    image_url = db.Column(db.String(), unique=False, nullable=True)

    def __init__(self, title, image_url):
        self.title = title
        self.image_url = image_url