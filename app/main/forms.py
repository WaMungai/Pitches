from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required 

class PitchForm(FlaskForm):
    '''
    Defines pitch column names and their data values
    '''
    title =StringField('Pitch title',validators =[Required()])
    text =TextAreaField('Text',validators=[Required()])
    cartegory= SelectField('Type',choices=[('pickup_pitches','Pickup-line pitches'),('interview','Interview pitch','product''Product pitch'),('promotion','Promotion pitch')],validators =[Required()])
    submit=SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    '''
    Class that updates user profile
    '''
    bio =TextAreaField('Bio',validators=[Required()])
    submit =SubmitField('Submit')
    
class CommentForm(FlaskForm):
    '''
    Defines columns for the comment form section
    '''
    text =TextAreaField('Leave a comment:',validators =[Required()])
    submit =SubmitField('Submit')