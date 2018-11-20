from wtforms import *
from wtforms.validators import *
from app.models.user import User

class Request_password_Form(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

class LoginForm(Request_password_Form):
    # email = StringField(validators=[DataRequired(), Length(8, 64),
    #                                 Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32)])



class RegisterForm(LoginForm):

    nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称至少需要两个字符,最多10个字符')])


    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已存在')

    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户名已存在')

class Forget_password_Form(Form):

    password1 = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32)])

    password2 = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32),EqualTo("password1",message='两次密码要一致')])


class Change_password_Form(Form):
    old_password = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32)])
    new_password1 = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32)])
    new_password2 = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入密码'), Length(6, 32),EqualTo("password1",message='两次密码要一致')])