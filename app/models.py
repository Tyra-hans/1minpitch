from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




class Pitches:
    '''
    Pitches class to define pitch objects
    '''
    def __init__(self,category,title,content,upvote,downvote):
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

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    image_file = db.Column(db.String(20), default='default.jpg')
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref= 'author', lazy=True)

    def __repr__(self):
        return f"User ('{self.username}' , '{self.email}' , '{self.image_file}')"


class Pitch(db.Model):
    id = db.Column(db.Integer,primary_key = 'True')
    title = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime,default =datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Pitch ('{self.title}' , '{self.date_posted}')"

    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)


    # def verify_password(self,password):
    #         return check_password_hash(self.pass_secure,password)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

            
    # def __repr__(self):
    #     return f'User {self.username}'