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
    index = db.Column(db.String(5))
    contestId = db.Column(db.Integer)
    pname = db.Column(db.String(64),unique=True)
    timeCons = db.Column(db.Integer)
    memoryCons = db.Column(db.Integer)
    passedTestCount = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('subs', lazy=True))
    
    def __init__(self,jsonin):
        self.id = jsonin['id']
        self.index = jsonin['problem']['index']
        self.pname = jsonin['problem']['name']
        self.contestId = jsonin['problem']['contestId']  ## It might be important to be certain from which part is this information is to be taken
        ## As it would be that the person would have solved the question in a competition and not directly in codeforces hence its to test if
        ## Author or problem is to be used in fetching contestid
        self.verdict = jsonin['verdict']
        self.timeCons = jsonin['timeConsumedMillis']
        self.memoryCons = jsonin['memoryConsumedBytes']
        self.passedTestCount = jsonin['passedTestCount']

    def __repr__(self):
        return '<Submission-'+self.verdict+'-'+str(self.id)+'>'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    handle = db.Column(db.String(64),index = True, unique=True)

    def reg(self):
        jsonin={}
        self.subs.append(Submission(jsonin))
    
    def __repr__(self):
        return '<User-'+str(self.handle)+'>'



