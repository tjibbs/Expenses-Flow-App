from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import db
from flask_restx import Api
from .auth import auth


DB_NAME = "expenses.sql"


# api = Api(title="Expenses work flow",
#   description="This automate Expenses request", version=1.0)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hjjhsjj hgjgggg'

# Importing the auth and views routs file
    from .views import views
    from .auth import auth

# Registering the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)

    # initializing and creating the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # app.init_app(app)
    # app.add_namespace(auth)

    return app
