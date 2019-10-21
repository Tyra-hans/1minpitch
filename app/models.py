from . import db

class Pitches:
    '''
    Pitches class to define pitch objects
    '''
    def __init__(self,category,title,content,upvote,downvote) :
        self.category= category
        self.title = title
        self.content = content
        self.upvote = upvote
        self.downvote = downvote

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    
    
    def __repr__(self):
        return f'User {self.name}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'