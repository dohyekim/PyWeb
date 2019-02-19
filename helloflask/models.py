from helloflask.init_db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref


class User(Base):
    # Table created at Mysql5(workbench)
    __tablename__='User'

    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True)
    username = Column(String, unique=True)
    passwd = Column(String)
    
    #None = null;
    def __init__(self, username, passwd, email=None):
        self.email = email
        self.username = username
        self.passwd = passwd

    #tostring
    def __repr__(self):
        return '%s, %s, %s' %(self.email, self.username, self.passwd)

class Post(Base):

    __tablename__='Post'

    postid = Column(Integer, primary_key = True)
    title = Column(String(256))
    date_posted = Column(TIMESTAMP)
    content = Column(String(1024))
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User')

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return 'Post %r, %r' %(self.title, self.date_posted)

# class Album(Base):
#     __tablename__ = 'Album'

#     album_id = Column(String(50), primary_key = True)
#     album_title = Column(String)
#     album_genre = Column(String)
#     rating = Column(Float(3,2))
#     releasedt = Column(String)
#     album_comp = Column(String(128))
#     entertainment = Column(String(128))
#     crawldt = Column(TIMESTAMP)
#     songs = relationship('Song', backref = backref('Song'))

        
#     def __repr__(self):
#         return '%s, %s, %s, %s,%s, %s, %s, %s,%s' %(self.album_id, self.album_title, self.album_genre, self.rating, self.releasedt, self.album_comp, self.entertainment, self.crawldt)



# class Song(Base):
#     __tablename__ = 'MS_Song'

#     song_no = Column(String(50), primary_key = True)
#     title = Column(String(128))
#     genre = Column(String(50))
#     album_id = Column(String(50), ForeignKey("Album.album_id"))
#     # join을 위해 가상의 column을 만든다
#     album = relationship('Album')
#     songsinger = relationship('SongSinger')

#     def __init__(self, song_no, title, genre, album_id):
#         self.song_no = song_no
#         self.title = title
#         self.genre = genre
#         self.album_id = album_id
    
#     def __repr__(self):
#         return '%s, %s, %s, %s' %(self.song_no, self.title, self.genre, self.album_id)


# class Singer(Base):
#     __tablename__ = 'Singer'

#     artist_id = Column(String(50), primary_key=True)
#     name = Column(String(100))
#     songsinger = relationship('SongSinger')

#     def __init__(self, artist_id, name):
#         self.artist_id = artist_id
#         self.name = name

#     def __repr__(self):
#         return '%s, %s' %(self.artist_id, self.name)

# class SongSinger(Base):
#     __tablename__ = 'SongSinger'

#     song_no = Column(String(50), ForeignKey('Song.song_no'))
#     artist_id = Column(String(50), ForeignKey('Singer.artist_id'))
#     # variables
#     song = relationship('Song')
#     singer = relationship('Singer')
#     __table_args__ = ( PrimaryKeyConstraint('song_no', 'artist_id'), {})

#     def __init__(self, song_no, artist_id):
#         self.song_no = song_no
#         self.artist_id = artist_id

#     def __repr__(self):
#         return '%s, %s' %(self.song_no, self.artist_id)


