from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_login import login_user , logout_user , current_user , login_required
#from data import Articles
# from flask_mysqldb import MySQL
from app.auth.forms import RegisterForm, ProfileEditForm
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
    import pdb
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user_obj = User(name = form.name.data, 
            email = form.email.data, 
            username = form.username.data, 
            password = form.password.data,
            address = form.address.data
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

@auth.route('/showProfile/<username>',methods=['GET','POST'])
@login_required
def view_profile(username):

    profile_editform = ProfileEditForm()
    if profile_editform.validate_on_submit():
        user_obj = User.query.filter_by(email=current_user.email).first()
        user_obj.username = profile_editform.username.data
        user_obj.email = profile_editform.email.data
        user_obj.address = profile_editform.address.data
        user_obj.contact = profile_editform.contact.data
        user_obj.gender = profile_editform.gender.data
        db.session.commit()
        flash('User profile update successfully.')
        return redirect(url_for('auth.view_profile',username=current_user))

    else:
        profile_editform.username.data = current_user.username
        profile_editform.email.data = current_user.email
        profile_editform.contact.data = current_user.contact
        profile_editform.address.data = current_user.address
        profile_editform.gender.data = current_user.gender

    return render_template('auth/view_profile.html',form=profile_editform)

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