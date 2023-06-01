from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    staff_id = db.Column(db.Integer)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    department = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class Expenses(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    expense_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(250))
    status = db.Column(db.String(20))
    submitter_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())


class Approver(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    approver_id = db.Column(db.Integer)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)


class Approvals(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    approval_id = db.Column(db.Integer)
    expense_id = db.Column(db.Integer)
    approval_id = db.Column(db.Integer)
    approved_at = db.Column(db.DateTime(timezone=True), default=func.now())
