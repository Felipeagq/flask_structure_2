from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import os

db = SQLAlchemy()
migrate = Migrate()

from config import DB_PATH

def create_app(setting_name):
    app = Flask(__name__)
    app.config.from_object(config[setting_name])

    db.init_app(app)
    if os.path.exists(DB_PATH):
        from app.schemas.users import Users
        migrate.init_app(app,db)
    else:
        db.create_all()
        from app.schemas.users import Users
        migrate.init_app(app,db)

    from app.routes.hello_check_route import hello_check_bp
    app.register_blueprint(hello_check_bp)

    from app.routes.insert_route import insert_bp
    app.register_blueprint(insert_bp)

    from app.routes.read_route import read_bp
    app.register_blueprint(read_bp)

    from app.routes.login_route import login_db
    app.register_blueprint(login_db)


    return app