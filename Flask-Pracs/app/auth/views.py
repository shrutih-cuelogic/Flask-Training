from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
# from flask_mysqldb import MySQL
from app.auth.forms import RegisterForm
# from passlib.hash import sha256_crypt
# from functools import wraps
from . import auth
# Config MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'flask_blog_app'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
# mysql = MySQL(app)

# Define the blueprint: 'auth', set its url prefix: app.url/auth

# Index
@auth.route('/')
def index():
    return render_template('index.html')

# # About
# @auth.route('/about')
# def about():
#     return render_template('auth/about.html')

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

# User Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    import pdb; pdb.set_trace();
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

    
        # # Create cursor
        # cur = mysql.connection.cursor()

        # # Execute query
        # cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # # Commit to DB
        # mysql.connection.commit()

        # # Close connection
        # cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)