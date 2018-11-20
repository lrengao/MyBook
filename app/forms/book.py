
from wtforms import Form, StringField, IntegerField
from wtforms.validators import *

class SearchForm(Form):
    q = StringField(validators=[DataRequired(),length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)




class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired(),Length(
        min=2,max=20,message='收件人姓名长度必须在2到20个字符之间')])

    mobile = StringField(validators=[DataRequired(),Regexp('^1[0-9]{10}$',0,'请输入正确的手机号')])

    message = StringField()

    address = StringField(validators=[DataRequired(),
                                      Length(min=10,max=70,
                                             message='地址还不到10个字吗,请尽量写详细些吧')])
#
# def search_q(q):
#     if 1<=len(q)<=30:
#         return True
#     return False
#
# def search_page(page):
#     if type(page) is int:
#         if 1<=page<=99:
#             return page
#     if not page:
#         return 1
#     return 1

