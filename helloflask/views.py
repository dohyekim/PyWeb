
from helloflask import app
from flask import Flask, g, Response, make_response, request, session, render_template, Markup, flash, redirect, url_for
from helloflask.forms import RegistrationForm, LoginForm, PostForm
from helloflask.init_db import init_database, db_session
from helloflask.models import Song, Album, SongSinger, Singer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import subqueryload, joinedload


@app.route('/sql')
def sql():
    res = Song.query.filter(Song.genre == "Ballad")
    return render_template('sqltest.htm', title="sql test", res = res)

@app.route('/sql2')
def sql2():
    res = db_session.query(Song).options(subqueryload(Song.album)).filter_by(genre = "Ballad").options(subqueryload(Song.songsinger)).options(subqueryload(Song.songsinger.singer))
    return render_template('sqltest.htm', title="sql test(join)", res = res)

@app.route('/sql3')
def sql3():
    res = db_session.query(Album).options(subqueryload(Album.songs))

    return render_template('sqltest.htm', title="sql test (n:1)", res = res)

@app.route('/sql4')
def sql4():
    res = db_session.query(Song).options(subqueryload(Song.songsinger))
    # ret = db_session.query(Singer).options(subqueryload(Singer.songsinger))

    return render_template('sqltest.htm', title="sql test (n:n) ", res = res)


@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.htm', title="Main Page")

@app.route('/register', methods=['GET','POST'])
def register():
    register = RegistrationForm()
    if register.validate_on_submit():
        flash('Account created for {}'.format(register.username.data), 'success')
        return redirect(url_for('main'))
    return render_template('register.html', title="Register Page", register = register)

@app.route('/login', methods=['GET','POST'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('main'))
    else:
        flash('Login Unsuccessful! Please check username and password', 'danger')
    return render_template('login.html', title="Login Page", login=login)

# @app.route('/post/new', methods=['GET','POST'])
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('python'))
#     return render_template('create.html', title="New Post", form=form)

@app.route('/python', methods=['GET','POST'])
def python():
    register = RegistrationForm()
    login = LoginForm()
    if register.validate_on_submit():
        flash('Account created for {}'.format(register.username.data), 'alert-success')
        return redirect(url_for('python'))
    return render_template('python.htm', title = "python",register = register, login=login)
    


