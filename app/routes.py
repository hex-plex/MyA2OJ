from flask import render_template, flash, redirect, url_for,request
from app import app,db
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.Form import LoginForm
from app.models import User
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET'])
def signUp1():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    return render_template('login.html', title='Sign-In', form = form )

@app.route('/signup',methods=['POST'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        message = None
        try:
            csa = CodeforcesSemiApi(form.handle.data)
            check=True
        except Exception as e:
            message=e
            check = False
        if not check:
            flash( 'No Such handle found' if message is None else message)
            return redirect(url_for('signUp1'))
        user = User.query.filter_by(handle=form.handle.data).first()
        if user is None:
            user = User(handle=form.handle.data)
            user.refresh()
            db.session.add(user)
            db.session.commit()
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('index'))
    else:
        flash('Please Input Handle')
        return redirect(url_for('signUp1'))        


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signUp1'))

@app.route('/switch')
def switch():
    logout_user()
    return redirect(url_for('signUp1'))

@login_required
@app.route('/feed',methods=['GET'])
def feed():
    current_user.refresh()
    task=list([])## this maybe stored in the task space or in a list of two do somewhere else
    if len(task)==0:
        return render_template('task.html',title="TASK",comple = "No Tasks Remaining Yet")
    else:
        return render_template('task.html',title="TASK",task=task[0])

@login_required
@app.route('/info')
def info():
    csa = CodeforcesSemiApi(current_user.handle,fetch=False)
    biolink=csa()
    ## Here maybe a bit BeatifulSoup can be applied to get the profile in a nice manner
    ## And have a minimiliztic form
    return redirect(biolink)
