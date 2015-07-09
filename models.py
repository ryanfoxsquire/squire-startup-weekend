# from https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

from catseverywhere import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Candidates(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(255))    
    last_name = db.Column(db.String(255))
    party = db.Column(db.String(255))
    picture_url = db.Column(db.String(255))
    twitter_url = db.Column(db.String(255))
    facebook_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, params):
        self.first_name = params.get('first_name', None)
        self.last_name = params.get('last_name', None)
        self.party = params.get('party', None)
        self.picture_url = params.get('picture_url', None)
        self.twitter_url = params.get('twitter_url', None)
        self.facebook_url = params.get('facebook_url', None)
        self.created_at = params.get('created_at', None)
        self.updated_at = params.get('updated_at', None)
