#RFS: from https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'  
    if("DATABASE_URL" in os.environ.keys()):
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    else:
        SQLALCHEMY_DATABASE_URI = "postgresql://localhost/wordcount_dev" #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print(SQLALCHEMY_DATABASE_URI)

class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


#class StagingConfig(Config):
#    DEVELOPMENT = True
#    DEBUG = True
#

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


#class TestingConfig(Config):
#    TESTING = True