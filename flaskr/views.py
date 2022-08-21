import functools

from flask import (
    Blueprint, g, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.get('/')
def get_home():
   return render_template('views/index.html') 

@bp.post('/')
def post_home():
    pass