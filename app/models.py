
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True) 

class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(20), nullable=True)
    end_date = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('educations', lazy=True))

class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(20), nullable=True)
    end_date = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('experiences', lazy=True))

class Skill(db.Model):
    __tablename__ = 'skill'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=True)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('skills', lazy=True))
