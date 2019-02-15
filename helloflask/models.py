from helloflask.init_db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    # 만든 테이블 이름
    __tablename__='User'

    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True)
    nickname = Column(String)
    passwd = Column(String)
    
    #None = null;
    def __init__(self, email=None, nickname='손님', passwd='11'):
        self.email = email
        self.nickname = nickname
        self.passwd = passwd

    #tostring
    def __repr__(self):
        return 'User %s, %r, %r, password=%r' %(self.id, self.email, self.nickname, self.passwd)