from flask import Flask , Blueprint
from flask_sqlalchemy import SQLAlchemy
from routes.players_routes import players_bp
from models import db
from services import read_from_api

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
result22 = read_from_api('http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season/2022')
result23 = read_from_api('http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season/2023')
result24 = read_from_api('http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season/2024')




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)