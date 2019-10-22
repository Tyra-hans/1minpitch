from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired , Length, Email, EqualTo
from flask_bootstrap import Bootstrap


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators = [DataRequired(), Length(min = 2, max = 20)])

    email = StringField('Email' ,
                        validators =  [DataRequired(), Email()])

    password = PasswordField('Password',validators = [DataRequired()] )
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')] )
    submit = SubmitField('Sign Up')

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
    