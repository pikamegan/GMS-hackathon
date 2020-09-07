from app import app, db
from flask import render_template, json, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token
from app.models import Users

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]  # required
        password = request.json["password"]  # required
    except KeyError:
        return jsonify(msg="You need to provide at least email and password to register."), 400
    return render_template("register.html")


@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        email = request.json["email"]
        password = request.json["password"]
    user = Users.query.filter_by(email=email, password=password).first()
    if user:
        access_token = create_access_token(email)
        return jsonify(msg="User logged in", access_token=access_token), 200
    else:
        return jsonify(msg="wrong email password"), 400

@app.route("/home")
def home():
    return render_template("home.html")

