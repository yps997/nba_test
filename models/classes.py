from . import db

# table\class of player
class Player(db.Model):
    _player_id = db.Column(db.String(150), primary_key=True)
    _name = db.Column(db.String(80), nullable=True)
    _twoPercent = db.Column(db.Float, nullable=False)
    _threePercent = db.Column(db.Float, nullable=False)


    # Relationship with PlayerSeason
    playerSeasons = db.relationship('PlayerSeason', backref='player', lazy=True)

#Department with game detailsof a player by season
class PlayerSeason(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
    _season = db.Column(db.Integer, nullable=True)
    _points_count = db.Column(db.Integer, nullable=False)
    _games_count = db.Column(db.Integer, nullable=False)
    _position = db.Column(db.String(80), nullable=True)
    _team = db.Column(db.String(80), nullable=True)
    _atr = db.Column(db.Float, nullable=False)
    _ppg = db.Column(db.Float, nullable=False)


