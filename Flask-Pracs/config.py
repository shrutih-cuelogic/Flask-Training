# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/testuser'
    SECRET_KEY = 'b240ac48e41e84a4278d195092289a8bdb08556b22f6760d'
    SQLALCHEMY_TRACK_MODIFICATIONS =True
    FIXTURE_DIRS = (
       'app/auth/fixtures/',
    )


class TestConfig(Config):
    """docstring for TestConfig"""
    
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/tdd_userblog'
    SECRET_KEY = 'b240ac48e41e84a4278d195092289a8bdb08556b22f6760d'
    SQLALCHEMY_TRACK_MODIFICATIONS =False