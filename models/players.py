from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

    class Player(db.Model):
        _player_id = db.Column(db.Integer, primary_key=True)
        _name = db.Column(db.String(80), nullable=True)
        _twoPercent = db.Column(db.Float, nullable=False)
        _threePercent = db.Column(db.Float, nullable=False)
        _city = db.Column(db.String(80), nullable=True)

        # Relationship with PlayerSeason
        playerSeason  = db.relationship('PlayerSeason ', backref='player', lazy=True)

    def __repr__(self):
        return f'<User {self.name} >'
