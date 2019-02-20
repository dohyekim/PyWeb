
from helloflask import app
from flask import Flask, g, Response, make_response, request, session, render_template, Markup, flash, redirect, url_for
from helloflask.forms import RegistrationForm, LoginForm, PostForm
from helloflask.init_db import init_database, db_session
from helloflask.models import User, Post
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy.sql import func


# def sql():
#     res = Song.query.filter(Song.genre == "Ballad")
#     return render_template('sqltest.htm', title="sql test", res = res)

# @app.route('/sql2')
# def sql2():
#     res = db_session.query(Song).options(subqueryload(Song.album)).filter_by(genre = "Ballad").options(subqueryload(Song.songsinger, SongSinger.singer))
#     return render_template('sqltest.htm', title="sql test(join)", res = res)

# @app.route('/sql3')
# def sql3():
#     res = db_session.query(Album).options(subqueryload(Album.songs))

#     return render_template('sqltest.htm', title="sql test (n:1)", res = res)

@app.route('/post/<postid>')
def post(postid):
    postno = db_session.query(Post).options(subqueryload(Post.user)).filter(Post.postid == postid).first()
    return render_template('postdetail.htm', title=postno.title ,postno = postno)
    # song = Song.query.filter_by(songno = songno).first()
    # songinfos = SongInfo.query.filter_by(songno = songno)
    # print("===>", songinfos.count())
    # return render_template("songinfo.html", song=song, songinfos=songinfos)

@app.route('/post/new', methods=['GET','POST'])
def new_post():
    form = PostForm()
    if session.get('loginUser'):
        loginUser = session.get('loginUser')
    else:
        session['next'] = request.url
        return redirect('/login')
    if session.get('loginUser') and form.validate_on_submit():
        post = Post(form.title.data, form.content.data, loginUser.get('userid'))
        try:
            db_session.add(post)
            db_session.commit()
            flash('Your post has been created!', 'success')
        except:
            db_session.rollback()
        return redirect(url_for('posting'))
    return render_template('create.htm', title="New Post", form=form)


@app.route('/posting', methods=['GET','POST'])
def posting():
    title = db_session.query(Post).first()
    posts = db_session.query(Post).options(subqueryload(Post.user))
    return render_template('posting.htm', title="Posting Page", postTitle = title, posts = posts)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.htm')

@app.route('/modal', methods=['POST'])
def modal():
    email = request.form.get('modalemail')
    passwd = request.form.get('modalpassword')
    u = User.query.filter('email = :email and passwd = sha2(:passwd, 256)').params(email = email, passwd=passwd).first()
        # 'email = :email and passwd = sha2(:passwd, 256)').params(email = email, passwd=passwd).first()
    if u is not None:
        session['loginUser'] = {'userid': u.id, 'username': u.username}
        flash('Login Success!')
        return redirect('/main')
    else:
        flash("Hmm, we don't recognize that email and(or) password. Please try again.")
        return render_template('login.htm', email = email)
 

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')
    u = User.query.filter('email = :email and passwd = sha2(:passwd, 256)').params(email = email, passwd=passwd).first()
    if u is not None:
        session['loginUser'] = {'userid': u.id, 'username': u.username}
        flash('Login Success!')
        if session.get('next'):
            nextpg = session.get('next')
            return redirect(nextpg)  
        return redirect('/main')
    else:
        flash("Hmm, we don't recognize that email and(or) password. Please try again.")
        return render_template('login.htm', email = email)   

@app.route('/logout')
def logout():
    if session.get('loginUser'):
        del session['loginUser']
    return redirect('/main')


@app.route('/register', methods=['GET','POST'])
def register_post():
    register = RegistrationForm()
    if register.validate_on_submit():
        flash('Account created for {}'.format(register.username.data), 'success')
        u = User(register.password.data, register.email.data,  register.username.data)
        try:
            db_session.add(u)

            db_session.commit()
            print("data inserted")
        except:
            db_session.rollback()

        return redirect('/login')

    return render_template('register.htm', title='Register Page', register = register)

@app.route('/board')
def board():
    return render_template('board.htm')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.htm', title="Main Page")




