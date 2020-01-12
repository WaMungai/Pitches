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
            
            return redirect(url_for('profile/update.html',form=form))
        
@main.route('/pitch/new',mrthods =['GET','POST'])
@login_required
def new_pitches():
    pitch_form =PitchForm()
    if pitch_form.validate_on_submit():
        title =pitch_form.title.data
        pitch =pitch_form.txt.datacategory = pitch_form.cartegory.data
        
        new_pitch =Pitch(title =tile,content =pitch,category=category,user=current_user,lokes=0,dislikes=0)
        
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    
    title ='New Pitch'
    return render_template('new_pitch.html',title=title,pitch_form=pitch_form)

@main.route('/pitches/interview_pitches')
def interview_pitches():
    pitches=Pitch.get_pitches('interview')
    
    return render_template("interview_piches.html",pitches=pitches)

@main.route('/pitches/product_pitches')
def product_pitches():
    pitches =Pitch.get_pitches('product')
    
    return render_template('product_pitches.html',pitches=pitches)

@main.route('/pitches/promotion_pitches')
def promotion_pitches():
    pitches =Pitch.get_pitches('promotion')
    
    return render_template('promotion_pitches.html',pitches =pitches)

@main.route('/pitch/<int:id>',method=['GET','POST'])
def pitch(id):
    pitch =Pitch.get_single_pitch(id)
    posted_date=pitche.posted.strftime'(%b %d,%Y')
    if request.args.get("like"):
        pitch.dislike =pitch..dislikes +1
        db.session.add(pitch)
        db.session.commit()
        
        return redirect("/pitches/{pitch_id}".format(pitch_id = pitch.id))
    
    comment_form.validate_on_submit():
        comment =comment_form.text.data
        
        new_comment=Comment(comment =comment,user_id =current_user,pitch_id=pitch)
        new_comment.save_comment()
        
        comments =Comments.get_comments(pitch)
        return.render_template("pitch.html",pitch=pitch,comment_form =comment_form,comments=comments,date=posted_date)
    
@main.route('/user/<uname>pitches')
def user_pitches(uname):
    user =User.query.filter_by(username=uname).first()
    pitches =Pitch.query.filter_by(user_id =user.id).all()
    pitches_count =Pitch.count_pitches(uname)
    
    return render_template("profile/pitches.html",user=user,pitches=pitches,pitches_count=pitches_count)    