from flask import Flask
from models.classes import Player, PlayerSeason
from models import db
import calculator_properties_for_objects
from services.calculator_properties_for_objects import Calculate_atr, Calculate_ppg
from processes.start_process import DICT_CALCULATE_POSATION

#position_average
def Create_objects(dct_players:dict):
    position_average =

    #בדיקה האם השחקן כבר קיים
    existing_player = Player.query.get(dct_players["playerId"])
    if existing_player:
        # עדכון שחקן קיים
        existing_player._twoPercent += dct_players['twoPercent']
        existing_player._threePercent += dct_players['threePercent']

    # אם שחקן לא קיים
    else:
        #יצירת שחקן חדש
     Player(
        _player_id=dct_players['playerId'],
        _name=dct_players['playerName'],
        _twoPercent=dct_players['twoPercent'],
        _threePercent=dct_players['threePercent']
    )
    #יצירת משימה (נוצר תמיד)
    PlayerSeason(
    _player_id = dct_players['playerId'],
    _season = dct_players['season'],
    _points_count = dct_players['points'],
    _games_count = dct_players['games'],
    _position = dct_players['position'],
    _team = dct_players['team'],
    _atr = dct_players["assists"] / dct_players["turnovers"],
    _ppg = (dct_players["points"] / dct_players["games"]) / position_average,
    )

            




