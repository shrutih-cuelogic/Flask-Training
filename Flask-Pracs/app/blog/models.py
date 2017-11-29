from datetime import datetime
from app import db, lm
from app.auth.models import User


#Define a Blog model
class Blog(db.Model):

    __tablename__ = 'user_blog'

    id = db.Column(db.Integer, 
        primary_key=True, 
        autoincrement=True
    )
    title = db.Column(db.String(128),  
        nullable=False
    )
    user_id = db.Column(db.Integer, 
        db.ForeignKey('auth_user.id'),
        nullable=False
    )
    description  = db.Column(db.String(),
        nullable=False
    )
    blog_created_on = db.Column(db.DateTime(), 
        default=datetime.utcnow
    )
    blog_updated_on = db.Column(db.DateTime(), 
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    published_status = db.Column(db.Boolean, 
        default=False
    )

    def __str__(self):
        return '<Blog %r>' % (self.title)
