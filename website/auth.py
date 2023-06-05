from . import db, auth
from flask_restx import Api, Resource, fields, Namespace
from flask import Blueprint, request, abort, redirect, url_for, render_template
from flask_restx import Api, Resource, fields
from . import db
from .models import User
from sqlalchemy import func

auth = Blueprint("auth", __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        data = request.get_json()
        staff_id = data.get("staff_id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        department = data.get("department")
        email = data.get("email")
        password = data.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user is not None:
            abort(400, "Email already exists. Login")
        else:
            new_user = User(
                staff_id=staff_id,
                first_name=first_name,
                last_name=last_name,
                department=department,
                email=email,
                password=password
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("auth.login"))
    else:
        return render_template("sign-up.html")


@auth.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


# @auth.route('/sign-up')
# class Sign_up(Resource):
#     def post(self):
#         data = request.get_json()
#         staff_id = data.get("staff_id")
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         department = data.get("department")
#         email = data.get("email")
#         password = data.get("password")

#         existing_user = User.query.filter_by(email=email).first()

#         if existing_user is not None:
#             abort(400, "Email already exists. Login")
#         else:
#             new_user = User(
#                 staff_id=staff_id,
#                 first_name=first_name,
#                 last_name=last_name,
#                 department=department,
#                 email=email,
#                 password=password
#             )
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for("auth.login"))

#     def get(self):
#         return render_template("sign_up_page.html")


# @auth.route('/login')
# class Login(Resource):
#     def post(self):
#         email = request.form.get("email")
#         password = request.form.get("password")

#         existing_user = User.query.filter_by(email=email).first()

#         if existing_user is None:
#             abort(400, "Wrong email address")
#         elif not existing_user.check_password(password):
#             abort(400, "Wrong password")
#         else:
#             # Perform further actions, such as generating a token or setting session data
#             return {'message': 'Login successful'}
