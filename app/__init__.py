from flask import Flask 
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail
from flask_login import LoginManager
from flask_simplemde import SimpleMDE 

boostrap =Bootstrap()
db =SQLAlchemy()
mail=Mail

login_manager =LoginManger()
login_manager.session_protrction ='strong'
login_manager.login_view ='auth.login'

simple =SimpleMDE()

def create_app(config_name):
    app= Flask(__name__)
    app.config.form_object(config_options[config_name])
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from .main import main as main_bluperint
    app.register_blueprint(main_blueprint)
    
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_bllueprint)
    
    return app