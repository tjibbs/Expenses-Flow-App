from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from flask_restx import Api
from .auth import auth


DB_NAME = "expenses.sql"


api = Api(title="Expenses work flow",
          description="This automate Expenses request", version=1.0)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hjjhsjj hgjgggg'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)
    # initializing and creating the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.init_app(app)
    api.add_namespace(auth)

    return app
