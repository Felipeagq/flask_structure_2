import os 
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.getcwd()
DB_PATH = os.path.join(BASE_PATH,"database.db")

class Config(object):
    DEBUG:bool = False
    SECRET_KEY:str = os.getenv("SECRET_KEY") or "Camila@luna"
    SQLALCHEMY_DATABASE_URI:str= f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS:bool = False
    FLASK_APP="entrypoint.py"


class ProductionConfig(Config):
    SECRET_KEY:str = os.getenv("SECRET_KEY") or "Camila@luna@Produccion"


class DevelopmentConfig(Config):
    DEBUG:bool = True



config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}