from flask_wtf import Flaskform
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo 
from wtforms import ValidationError 
from  .. models import User

class RegistrationForm(FlaskForm):
    email =StringField('Your email address',validators=[Required(),Email()])
    username =StringField('Enter your username',validators =Required[Required()])
    password =PasswordField('Password',validators=[Required(),EqualTo('password_confrim',message='Passwords must match')])
    password_confirm =PasswordField('Confirm Passwords',validators =[Required()])
    submit =SubmitField('Sign up')
    
    def validate_email(self,data_field):
        if User.query.filte_by(email=data_field.data).first():
            raise ValidationErrord('There is an account with that email')
        
    def validate_username(self,data_field):
        if User.qury.filter_by(username=data_field.data).first():
            raise Validatiinerror('That username is taken')
        
class Login Form(FlaskForm):
    email =StringField('Your Email Address',validators =[Required(),Email()])
    password =PasswordField('Password',validators=[Required()])
    remember =BooleanField('Remember me')
    submit =SubmitField('Sign In')