from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route("/", methods=["GET"])
def Home():
    return render_template("home.html")


@views.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


@views.route("/expenses_claim_form", methods=["GET"])
def claimForm():
    return render_template("expenses_claim_form.html")


@views.route("/approval_page", methods=["GET"])
def ApprovalPage():
    return render_template("approval_page.html")
