from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_login import login_user , logout_user , current_user , login_required
#from data import Articles
# from flask_mysqldb import MySQL
from app.auth.forms import RegisterForm
# from passlib.hash import sha256_crypt
# from functools import wraps
import json
from . import auth
from .. import db
from models import User, Blog

# Define the blueprint: 'auth', set its url prefix: app.url/auth

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
    return redirect(url_for('auth.blog_home') or url_for('index'))

@auth.route('/blogHome')
@login_required
def blog_home():
    return render_template('auth/blog_home.html')

@auth.route('/showAddBlog')
@login_required
def show_add_blog():
    return render_template('auth/add_blog.html')

@auth.route('/addBlog',methods=['POST'])
@login_required
def add_blog():
    # published_status = False
    if current_user:
        user = current_user
        if request.form['inputTitle'] and request.form['inputDescription']:
            blog_obj = Blog(title = request.form['inputTitle'], 
                description = request.form['inputDescription'],
                user_id = user.id
                )
            db.session.add(blog_obj)
            if blog_obj:
                db.session.commit()
                # published_status = True
                flash('You have successfully created your blog', 'success')
                return redirect(url_for('auth.blog_home'))
            else:
                return render_template('error.html',error = 'An error occurred!')
        else:
            flash('Please enter blog details' , 'error')

@auth.route('/getBlog')
@login_required
def getBlog():
    try:
        if current_user:
            blogs = current_user.blogs.all()
            if blogs:
                blogs_list = []
                for blog in blogs:
                    blog_dict = {
                        'user_id' : blog.user_id,
                        'title' : blog.title,
                        'description' : blog.description,
                        'publication_date' : str(blog.publication_date)
                    }
                    blogs_list.append(blog_dict)

                return json.dumps(blogs_list)
            else:
                return render_template('error.html', error = 'Current user has no blogs')
        else:
            return render_template('error.html', error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error = str(e))

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