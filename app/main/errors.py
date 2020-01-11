from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render 404 error page when the page does not show
    '''
    return render_template(404.html),404
