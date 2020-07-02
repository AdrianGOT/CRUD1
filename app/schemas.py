from app import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)

class Info(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    usuario = db.Column(db.String(10), nullable = False)
    name = db.Column(db.String(10), nullable = False)
    lastName = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(10),unique = True , nullable = False)
    time = db.Column(db.String(20), nullable = False)