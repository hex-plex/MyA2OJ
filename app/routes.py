from flask import render_template, flash, redirect, url_for,request
from app import app
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/signup',methods=['GET'])
def signUp():
    return render_template('signup.html')


@app.route('/signup',methods=['POST'])
def signUp():
    
    return render_template('signup.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template

@app.route('/switch')
def switch():
    logout_user()
    return render_template('login.html')

@login_required
@app.route('/info')
def info():
    return render_template('info.html')
