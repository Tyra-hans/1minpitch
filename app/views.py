from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from app import app

#views
pitches = [
    {
        'author' : 'Tyra Hans' ,
        'title' : 'Pitch 1',
        'content' : 'First pitch content',
        'date_posted' : 'April 20,2019'
    },
    {
        'author' : 'Trevor TheTrev' ,
        'title' : 'Pitch 2',
        'content' : 'Second pitch content',
        'date_posted' : 'May 6,2019'
    },
]

@app.route('/')
def home():
    return render_template('index.html', posts = pitches)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about' )

@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = register ,form = form)

@app.route('/login',methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))

        else:
            flash('Login failed. Please check username and password','danger')
    return render_template('login.html', title = login ,form = form)
