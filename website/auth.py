from flask import Blueprint, request, abort
from flask_restx import Api, Resource, fields, Namespace
from . import db
from .models import User
from sqlalchemy import func


auth = Namespace("auth", __name__)


sign_up_model = auth.model(
    "User",
    {
        "staff_id": fields.Integer(required=True, description="Staff id number"),
        "first_name": fields.String(required=True, description="Your first name"),
        "last_name": fields.String(required=True, description="Your last name"),
        "department": fields.String(description="Your department"),
        "email": fields.String(required=True, description="Eneter a valid email Address"),
        "password": fields.String(required=True, description="Your password must contain a special character")
    }
)


login_model = auth.model(
    "Expenses",
    {
        "expense_id": fields.Integer(required=True, description="Expense ID"),
        "amount": fields.String(required=True, description="Amount required"),
        "description": fields.String(),
        "status": fields.String(),
        "submitter_id": fields.Integer(),
        "category_id": fields.Integer(),
        # "created_at": fields.DateTime(timezone=True, default=func.now(), format="%Y-%m-%dT%H:%M:%S"),

    }
)


@auth.route('/sign-up')
class Sign_up(Resource):
    @auth.marshal_with(sign_up_model, code=201)
    @auth.expect(sign_up_model)
    def post(self):
        data = request.get_json()
        staff_id = data.get("staff_id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        department = data.get("department")
        email = data.get("email")
        password = data.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user is not None:
            abort(400, "Email already exist. Login")
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
            return {"Registration successful"}

    def get(self):
        return {"message": "hello wolrd"}


@auth.route('/login')
class Login(Resource):
    @auth.marshal_with(login_model, code=201)
    @auth.expect(login_model)
    def get(self):
        email = auth.payload.get("email")
        password = auth.payload.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user is None:
            abort(400, "Wrong email address")
        elif not existing_user.check_password(password):
            abort(400, "Wrong password")
        else:
            # Perform further actions, such as generating a token or setting session data
            return {'message': 'Login successful'}

#     def get(self):
#         return {"message": "hello wolrd"}
# @auth.route('/logout')
# def logout():
#     return "<p>Logout Page</p>"
