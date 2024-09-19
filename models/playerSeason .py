from flask_sqlalchemy import SQLAlchemy
from app import db

    class PlayerSeason (db.Model):
        _id = db.Column(db.Integer, primary_key=True)
        _player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
        _season = db.Column(db.Integer, nullable=True)
        _points_count = db.Column(db.Integer, nullable=False)
        _games_count = db.Column(db.Integer, nullable=False)
        _position = db.Column(db.String(80), nullable=True)
        _team = db.Column(db.String(80), nullable=True)
        _atr = db.Column(db.Float, nullable=False)
        _ppg = db.Column(db.Float, nullable=False)




    def __repr__(self):
        return f'<User {self.name} >'