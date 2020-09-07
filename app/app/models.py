from app import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(160), index=True, unique=True)
    fullname = db.Column(db.String(128))
    password = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
