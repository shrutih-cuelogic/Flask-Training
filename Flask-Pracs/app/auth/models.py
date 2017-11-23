# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from datetime import datetime
from app import db, lm
from flask_login import UserMixin

# # Define a base model for other database tables to inherit
# class Base(db.Model):

#     __abstract__  = True

#     id            = db.Column(db.Integer, primary_key=True)
#     date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
#     date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
#                                            onupdate=db.func.current_timestamp())

# Define a User model
class User(db.Model, UserMixin):

    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Name
    name = db.Column(db.String(128),  nullable=False)

    #User Name
    username  = db.Column(db.String(128),  nullable=False)
    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.String(192),  nullable=False)

    address = db.Column(db.String(192),  nullable=False)

    contact = db.Column(db.Integer, nullable=False)

    gender = db.Column(db.String(50),  nullable=False)

    blogs = db.relationship('Blog', backref='author',cascade="all,delete",lazy='dynamic')

    def __str__(self):
        return '<User %r>' % (self.username)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Define a Blog model
class Blog(db.Model):

    __tablename__ = 'user_blog'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(128),  nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'),
        nullable=False)

    description  = db.Column(db.String(128),  nullable=False)

    blog_created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    blog_updated_on = db.Column(db.DateTime(), default=datetime.utcnow,
                                          onupdate=datetime.utcnow)

    published_status = db.Column(db.Boolean, default=False)

    def __str__(self):
        return '<Blog %r>' % (self.title)
