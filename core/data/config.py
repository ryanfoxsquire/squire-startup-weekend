#RFS: from https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    print("Config Loaded")

class ProductionConfig(Config):
    DEBUG = False


#class StagingConfig(Config):
#    DEVELOPMENT = True
#    DEBUG = True
#

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


#class TestingConfig(Config):
#    TESTING = True