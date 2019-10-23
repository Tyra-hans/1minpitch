from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField,IntegerField
from wtforms.validators import DataRequired , Length, Email, EqualTo
from flask_bootstrap import Bootstrap
from wtforms import ValidationError
from ..models import User,Category
import wtforms
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def choice_query():
    cat = Category.query.all()
    return cat

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

class PitchForm(FlaskForm):
    pitch = StringField('Category' ,validators=[DataRequired()])
    title = StringField('Enter Your Name' ,validators=[DataRequired()])
    submit = SubmitField('Submit')

# choices =  Category.query.all()
class SharePitchForm(FlaskForm):
    # pitch_category = StringField('', validators=[Required()], render_kw={"placeholder": "Select pitch category"})
    
    # select option
    # pitch_category = SelectField(' Pitch here!', choices=choices)
    cat = QuerySelectField(query_factory=choice_query, allow_blank=True)
    pitch = TextAreaField('', validators=[DataRequired()], render_kw={"placeholder": "Write your pitch here :)"})
    # contributor_name = StringField('', validators=[Required()], render_kw={"placeholder":"Write your username"})
    # username should pick from current user's username
    submit = SubmitField('Submit')
    # category_select_field = wtforms.SelectField(label="Category")




class CommentForm(FlaskForm):
    description = StringField('Review title' ,validators=[DataRequired()])
    submit = SubmitField('Submit')  



    