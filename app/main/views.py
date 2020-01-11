from flask import render_template,request,redirect,url_for,abort
from .import main
from flask_login import login_required,current_user 
import datetime  
from ..models import User,Pitch,Comment  
from .. import db 
from .forms import UpdateProfile,PitchForm,CommentForm 

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data 
    '''
    title ="Pitch perfect"
    
    pickup_pitches =Pitch.get_pitches("pickup-line")
    interview_pitches =Pitch.get_pitches("interview")
    product_pitches =Pitch.get_pitches("product")
    promotion_pitches=Pitches.get_pitches("promotion")
    
    return render_template('index.html',title =title,pickup=pickup_pitches,interview=interview_pitches,product=product_pitches,promotion=promotion_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user =User.query,filter_by(username=uname).first()
    
    if user is None:
        abort(404)
        
        form =UpdateProfile()
        
        if form.valiidate_on_submit():
            user.bio =form.bio.data
            
            db.session.add(user)
            db.session.commit()