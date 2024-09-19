from flask import Blueprint, jsonify, request, render_template
from models import db
from models.classes import Player, PlayerSeason


players_bp = Blueprint('players', __name__, url_prefix='/api/players')




# URL: /api/players?position={position}&season={season}

VALID_POSITIONS = ['C', 'PF', 'SF', 'SG', 'PG']
@players_bp.route('/', methods=['GET'])
def get_players():
    position = request.args.get('position')
    season = request.args.get('season')

    if not position or position not in VALID_POSITIONS:
        return jsonify({"error": f"position {position} not exist"}), 404

    # query = db.session.query(Player).join(PlayerSeason)
    # query = query.filter(PlayerSeason._position == position)
