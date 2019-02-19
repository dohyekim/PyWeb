
from helloflask import app
from flask import Flask, g, Response, make_response, request, session, render_template, Markup, flash, redirect, url_for
from helloflask.forms import RegistrationForm, LoginForm, PostForm
from helloflask.init_db import init_database, db_session
from helloflask.models import User, Post
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import subqueryload, joinedload


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


@app.route('/posting', methods=['GET','POST'])
def posting():
    title = db_session.query(Post).first()
    return render_template('posting.htm', title="Posting Page", postTitle = title)
    # register = RegistrationForm()
    # login = LoginForm()
    # if register.validate_on_submit():
    #     flash('Account created for {}'.format(register.username.data), 'alert-success')
    #     return redirect(url_for('python'))
    # return render_template('posting.htm', title = "Posting Page",register = register, login=login)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.htm')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')
    u = User.query.filter('email = :email and passwd = sha2(:passwd, 256)').params(email = email, passwd=passwd).first()
    if u is not None:
        session['loginUserid'] = u.id
        session['loginUsername'] = u.username
        return redirect('/main')
    else:
        flash("Hmm, we don't recognize that email and(or) password. Please try again.")
        return render_template('login.htm', email = email)    
    
# @app.route('/register', methods=['GET'])
# def register():

#     return render_template('register.htm', title='Register Page')

@app.route('/register', methods=['GET','POST'])
def register_post():
    register = RegistrationForm()
    if register.validate_on_submit():
        flash('Account created for {}'.format(register.username.data), 'success')
        u = User(register.email.data, register.username.data, register.password.data)
        try:
            db_session.add(u)

            db_session.commit()
            print("data inserted")
        except:
            db_session.rollback()

        return redirect('/login')

    return render_template('register.htm', title='Register Page', register = register)

# @app.route('/login', methods=['GET', POST'])
# def login():

#     login = LoginForm()
#     if login.validate_on_submit():
#         flash('You have been logged in!', 'success')
#         return redirect(url_for('main'))
#     else:
#         flash('Login Unsuccessful! Please check username and password', 'danger')
#     return render_template('login.htm', title="Login Page", login=login)

@app.route('/logout')
def logout():
    if session.get('loginUserid'):
        del session['loginUserid']
        del session['loginUsername']
    return redirect('/main')

@app.route('/board')
def board():
    return render_template('board.htm')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.htm', title="Main Page")



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



