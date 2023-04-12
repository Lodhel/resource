from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Configuration')

db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_size=20, pool_recycle=3600)
migrate = Migrate(app, db)
