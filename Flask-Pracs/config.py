# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/testuser'
    SECRET_KEY = 'b240ac48e41e84a4278d195092289a8bdb08556b22f6760d'
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  
    SQLALCHEMY_TRACK_MODIFICATIONS =True