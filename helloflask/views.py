
from helloflask import app
from flask import Flask, g, Response, make_response, request, session, render_template, Markup, flash, redirect, url_for
from forms import RegistrationForm, LoginForm, PostForm
from helloflask.init_db import init_database, db_session
from helloflask.models import User, Post
from sqlalchemy.exc import SQLAlchemyError

@app.route('/')
def sqltest():
    ret = 'aaaa'

    try:
        u = User('abc@abc.com', 'Hong')
        # db_session.add(u)
        ret = User.query.all()
        db_session.commit()
        retf = User.query.filter(User.id > 10)
        aa = User.query.filter(User.id == 11).first()
        aa.email = 'zxc@vbnm.asd'
        db_session.add(aa)
        bb = User.query.filter(User.id == 22).first()
        db_session.delete(bb)
        db_session.commit()
        # db_session.delete(u)
        # db_session.commit()

    except SQLAlchemyError as sqlErr:
        print(sqlErr)
        db_session.rollback()
    except:
        print('Errorrrrrrr!')

    return render_template('a.htm', title="sql", userlist = ret, filtereduser = retf)

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

@app.route('/post/new', methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('python'))
    return render_template('create.html', title="New Post", form=form)

@app.route('/python', methods=['GET','POST'])
def python():
    register = RegistrationForm()
    login = LoginForm()
    if register.validate_on_submit():
        flash('Account created for {}'.format(register.username.data), 'alert-success')
        return redirect(url_for('python'))
    return render_template('python.htm', title = "python",register = register, login=login)
    


