from . import db

# table\class of player
class Player(db.Model):
    _player_id = db.Column(db.String(150), primary_key=True)
    _name = db.Column(db.String(80), nullable=True)
    _twoPercent = db.Column(db.Float, nullable=False)
    _threePercent = db.Column(db.Float, nullable=False)


    # Relationship with PlayerSeason
    playerSeasons = db.relationship('PlayerSeason', backref='player', lazy=True)


