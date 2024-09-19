from . import db

# table\class of player
class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    twoPercent = db.Column(db.Float, nullable=False)
    threePercent = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(80), nullable=True)

    # Relationship with PlayerSeason
    playerSeasons = db.relationship('PlayerSeason', backref='player', lazy=True)


