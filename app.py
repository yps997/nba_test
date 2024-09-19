from flask import Flask , Blueprint
from flask_sqlalchemy import SQLAlchemy
from routes.players_routes import players_bp
from models import db
from services import read_from_api
from services.process_nba_json_data import process_nba_data
from processes.start_process import Run_process

#building and configuring the aplication and database

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba_stats.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(players_bp)

    with app.app_context():
        db.create_all()

    return app

#Receiving data and placing it in an appropriate object

#base url
URL_API = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season'
#list of season
SEASON_LST = ["2022","2023","2024"]
#start program
Run_process(URL_API, SEASON_LST)



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)