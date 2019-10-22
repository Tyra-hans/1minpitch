from flask import Flask,render_template, url_for, flash, redirect, request, abort
from .forms import RegistrationForm, LoginForm
from . import main
from ..models import Pitches,User,db
from flask_login import login_required, login_user

#views
pitchesexamples = [
    {
        'author' : 'Tyra Hans' ,
        'title' : 'Pitch 1',
        'category' : 'Business',
        'content' : 'First pitch content',
        'date_posted' : 'April 20,2019'
    },
    {
        'author' : 'Trevor TheTrev' ,
        'title' : 'Pitch 2',
        'category' : 'Pick-up lines',
        'content' : 'Second pitch content',
        'date_posted' : 'May 6,2019'
    },
    {
        'author' : 'Amy Lasu' ,
        'title' : 'Pitch 3',
        'category' : 'one-liners',
        'content' : 'Third pitch content',
        'date_posted' : 'June 7,2019'
    },
    {
        'author' : 'Dan Kioi' ,
        'title' : 'Pitch 4',
        'category' : 'puns',
        'content' : 'Fourth pitch content',
        'date_posted' : 'July 8,2019'
    },
    {
        'author' : 'Ren Baby' ,
        'title' : 'Pitch 5',
        'category' : 'one-liners',
        'content' : 'Fifth pitch content',
        'date_posted' : 'Aug 7,2019'
    },
]

@main.route('/')
def home():
    return render_template('index.html', posts = pitchesexamples)

@main.route('/about')
def about():
    return render_template('about.html', title = 'about' )

@main.route('/register', methods= ['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # import pdb; pdb.set_trace()
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        # import pdb; pdb.set_trace()
        return redirect(url_for('main.login'))
        flash(f'Account created for {form.username.data}!', 'success')
        
    return render_template('register.html', title = register ,form = form)

@main.route('/login',methods= ['GET', 'POST'])
def login():
    login_form = LoginForm()
    # import pdb; pdb.set_trace()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.pass_secure.data):
            login_user(user,login_form.remember.data)
            flash('You have been logged in!','success')
            return redirect(request.args.get('next') or url_for('main.profile'))
            # return render_template('profile.html')

        else:
            flash('Login failed. Please check username and password','danger')
        
        title = "onepitch login"
        
        

    # else:
        
        # return render_template(url_for('main.login'))

         
    return render_template('login.html', title = login ,login_form = login_form)

@main.route('/')
def pitches():
    return render_template('pitch.html', posts = pitches)

@main.route('/user/<email>')
def profile(email):
    import pdb; pdb.set_trace()
    email = email
    user = User.query.filter_by(email = email).first()
    if user is None:
        abort(404)

    return render_template("profile.html", user = user)



