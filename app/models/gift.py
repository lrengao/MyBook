from sqlalchemy import *
from sqlalchemy.orm import relationship


from app.spider.YuShuBook import YuShuBook
from .base import Base, db


class Gift(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean,default=False)


    def is_yourself_gift(self,uid):
        return True if self.uid == uid else False

    #赠送清单页面
    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched = False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status ==1).group_by(Wish.isbn).all()
        count_list =[{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list
    #最近上传相关代码 (主页)
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 最近上传相关代码 (主页)
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(30).distinct().all()
        return recent_gift

from app.models.wish import Wish