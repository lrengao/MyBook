from flask import Flask
from flask_login import login_manager,LoginManager
from .models.book import db
from flask_mail import Mail



login_manager = LoginManager()
mail = Mail()

def create_app():
    app =Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    #flask_sqlalchemy初始化
    db.init_app(app)
    login_manager.init_app(app)
    #没有登录跳转到某个页面
    login_manager.login_view = 'web.login'
    #进入登录页面的提示
    login_manager.login_message = "请先进行登录"
    mail.init_app(app)
    register_blueprint(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    #注册蓝图
    app.register_blueprint(web)