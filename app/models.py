from datetime import datetime
from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Submission(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    verdict = db.Column(db.String(64))
    User_id = db.Column(db.Integer, db.ForeignKey('User.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('Submissions', lazy=True))
    def __init__(self,jsonin):
        pass


class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    handle = db.Column(db.String(64),index = True, unique=True)
    
    def __repr__(self):
        return '<User-'+str(self.handle)+'>'



    ## THis should save the file
