from helloflask.init_db import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    # Table created at Mysql5(workbench)
    __tablename__='User'

    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True)
    username = Column(String, unique=True)
    passwd = Column(String)
    posts= relationship('Post', backref='author', lazy=True)
    
    #None = null;
    def __init__(self, email=None, username, passwd):
        self.email = email
        self.username = username
        self.passwd = passwd

    #tostring
    def __repr__(self):
        return 'User %s, %r, %r' %(self.id, self.email, self.username)

class Post(Base):
    id = Column(Integer, primary_key = True)
    title = Column(String)
    date_posted = Column(DateTime)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
    return 'Post %r, %r' %(self.title, self.date_posted)
