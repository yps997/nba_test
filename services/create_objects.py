from flask import Flask
from models.classes import Player, PlayerSeason
from models import db


def Create_objects(dct:dict):
    #בדיקה האם השחקן כבר קיים
    existing_player = Player.query.get(dct["playerId"])

    if existing_player:
        # עדכון שחקן קיים
        existing_player._twoPercent += dct['twoPercent']
        existing_player._threePercent += dct['threePercent']

    # אם שחקן לא קיים
    else:
        #יצירת שחקן חדש
     Player(
        _player_id=dct['playerId'],
        _name=dct['playerName'],
        _twoPercent=dct['twoPercent'],
        _threePercent=dct['threePercent']
    )
    #יצירת משימה (נוצר תמיד)
    PlayerSeason(
    _player_id = dct['playerId'],
    _season = dct['season'],
    _points_count = dct['points'],
    _games_count = dct['games'],
    _position = dct['position'],
    _team = dct['team'],
    _atr = dct [23],
    _ppg = dct[0],
    )
        """
        לחשב נקודות ואחוזי קליעה
        """
            




