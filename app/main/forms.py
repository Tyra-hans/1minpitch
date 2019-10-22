from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired , Length, Email, EqualTo
from flask_bootstrap import Bootstrap
from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators = [DataRequired(), Length(min = 2, max = 20)])

    email = StringField('Email' ,
                        validators =  [DataRequired(), Email()])

    password = PasswordField('Password',validators = [DataRequired()] )
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')] )
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    # user_id = StringField('user_id',validators=[DataRequired()])
    # user_name = StringField('user_name',validators=[DataRequired(), Length(min=3, max=20)])***
    email = StringField('Email', validators=[DataRequired(), Email()])
    pass_secure = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('remember', default=False)
    submit = SubmitField('LogIn')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    