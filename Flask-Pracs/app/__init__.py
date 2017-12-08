# Import flask and template operators
from flask import Flask
# from flask_mysqldb import MySQL
# #Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

# Import a module / component using its blueprint handler variable (mod_auth)


# Define the WSGI application object
app = Flask(__name__)
admin = Admin(app, name='sample', template_mode='bootstrap3')

# Configurations
app.config.from_object('config')
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.auth import views, models
from app.auth import auth as auth_blueprint

# Register blueprint(s)
app.register_blueprint(auth_blueprint)


# Build the database:
# This will create the database file using SQLAlchemy
admin.add_view(ModelView(models.User, db.session))

from app.auth.models import *

db.create_all()