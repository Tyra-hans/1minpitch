from flask import Flask,render_template, url_for, flash, redirect, request, abort
from .forms import RegistrationForm, LoginForm, UpdateProfile, PitchForm, SharePitchForm, CommentForm
from . import main
from ..models import Pitch,User,db , Comment
from flask_login import login_required, login_user , current_user
from .. import photos
from ..email import mail_message

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
        mail_message("Welcome to 1minpitch!","email/welcome_user",user.email,user=user)
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
            return redirect(url_for('main.profile', uname=user.username))
            # return render_template('profile.html')

        else:
            flash('Login failed. Please check username and password','danger')
        
        title = "minpitch login"
        
        

    # else:
        
        # return render_template(url_for('main.login'))

         
    return render_template('login.html', title = login ,login_form = login_form)

@main.route('/')
def pitches():
    return render_template('pitch.html', posts = pitches)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    # import pdb; pdb.set_trace()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data


        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('updateprof.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.image_file = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/business', methods=['GET','POST'])
@login_required
def business():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        # import pdb; pdb.set_trace()        
        business = Pitch(pitch=pitch_form.pitch.data,title = pitch_form.title.data)
        db.session.add(business)
        db.session.commit()
    business = Pitch.query.all()
    return render_template('business.html',business=business,pitch_form=pitch_form)

@main.route('/pitch', methods=['GET','POST'])
@login_required
def pitch():
    form = SharePitchForm()
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    # import pdb; pdb.set_trace()
    # import pdb; pdb.set_trace()
    pitch = Pitch(pitch=form.pitch.data,category=form.cat.data)
    db.session.add(pitch)
    db.session.commit()
    return render_template('pitch.html', form=form)

@main.route('/pickuplines', methods=['GET','POST'])
@login_required
def pickuplines():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        # import pdb; pdb.set_trace()        
        pickuplines = Pitch(pitch=pitch_form.pitch.data,title = pitch_form.title.data)
        db.session.add(pickuplines)
        db.session.commit()
    pickuplines = Pitch.query.all()
    return render_template('pickup_lines.html',pickuplines=pickuplines,pitch_form=pitch_form)

@main.route('/puns', methods=['GET','POST'])
@login_required
def puns():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        # import pdb; pdb.set_trace()        
        puns = Pitch(pitch=pitch_form.pitch.data,title = pitch_form.title.data)
        db.session.add(puns)
        db.session.commit()
    puns = Pitch.query.all()
    return render_template('puns.html',puns=puns,pitch_form=pitch_form)

@main.route('/oneliners', methods=['GET','POST'])
@login_required
def oneliners():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        # import pdb; pdb.set_trace()        
        oneliners = Pitch(pitch=pitch_form.pitch.data,title = pitch_form.title.data)
        db.session.add(oneliners)
        db.session.commit()
    oneliners = Pitch.query.all()
    return render_template('one-liners.html',oneliners=oneliners,pitch_form=pitch_form)



#routing for comments
@main.route('/comments/<int:id>', methods=['GET','POST'])
@login_required
def comment(id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        
        new_comment = Comment(comment_post=comment_form.description.data,pitch_id=id,user=current_user)
        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(pitch_id=id)
    
    return render_template('comment.html',comments=comments,comment_form=comment_form)









