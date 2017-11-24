from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_login import login_user , logout_user , current_user , login_required
#from data import Articles
# from flask_mysqldb import MySQL
from app.auth.forms import RegisterForm
# from passlib.hash import sha256_crypt
# from functools import wraps
import json
from datetime import datetime
from . import auth
from .. import db
from models import User


# Index
@auth.route('/')
def index():
    return render_template('index.html')

# User Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # import pdb; pdb.set_trace();
    if request.method == 'POST' and form.validate():
        user_obj = User(name = form.name.data, 
            email = form.email.data, 
            username = form.username.data, 
            password = form.password.data,
            address = form.address.data,
            contact = form.contact.data,
            gender = form.gender.data,
            )
        db.session.add(user_obj)
        db.session.commit()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


# Login
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    email = request.form['email']
    password = request.form['password']
    registered_user = User.query.filter_by(email=email,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('auth.login'))
    login_user(registered_user, True)
    flash('Logged in successfully')
    return redirect(url_for('blog_mod.blog_home') or url_for('index'))

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)