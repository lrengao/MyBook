from flask import render_template
from flask_login import current_user

from app.models.gift import Gift
from app.models.user import User
from app.view_models.book import BookViewModel
from . import web





@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books  = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html',recent = books)


@web.route('/personal')
def personal_center():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template('personal.html',user=user)
