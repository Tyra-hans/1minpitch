from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

    

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
    image_file = db.Column(db.String(20))
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    # password_hash = db.Column(db.String(255))
    pitches =  db.relationship('Pitch', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    #method that takes ,hashes and compares our password
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f"User ('{self.username}' , '{self.email}' , '{self.image_file}')"


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = 'True')
    title = db.Column(db.String(100), index = True)
    time = db.Column(db.DateTime,default =datetime.utcnow)
    pitch = db.Column(db.String(300), index = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(type_id = id).all()
        return pitches
    
    def __repr__(self):
        return f"Pitch ('{self.title}' , '{self.date_posted}')"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

            
    def __repr__(self):
        return f"User ('{self.title}' , '{self.category}' , '{self.content}')"

class Category(db.Model):
    __tablename__ = 'category'

    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), index = True)
    pitches = db.relationship('Pitch', backref = 'type', lazy = 'dynamic')

    @classmethod
    def get_categories(cls):
        types = Types.query.all()
        return types
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    comment_post = db.Column(db.String(255),index=True)
    time = db.Column(db.DateTime,default = datetime.utcnow )
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments
