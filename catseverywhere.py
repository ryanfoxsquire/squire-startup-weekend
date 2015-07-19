import os
from flask import Flask, render_template
from flask import request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from settings import APP_STATIC
from pdb import set_trace as pause
import requests
from scraping_tools import MyHTMLParser, get_twitter_avatar_img_url
import datetime

app = Flask(__name__)

# Set Config Settings
# THIS SHOULD BE config.ProductionConfig BEFORE PUSHING TO HEROKU
if("APP_SETTINGS" in os.environ.keys()):
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    APP_SETTINGS="config.DevelopmentConfig"  # "config.ProductionConfig"
    app.config.from_object(APP_SETTINGS)
    
#connect to database
db = SQLAlchemy(app)
from models import *

@app.route('/')
@app.route('/index')
def hello_world():
    candidates = Candidate.query.order_by(Candidate.smi.desc()).all()
    return render_template('index.html', rankings_list = candidates)

@app.route('/refresh_data')
def refresh_data():
    updates = []
    candidates = Candidate.query.all()
    for candidate in candidates:
        current_img_url = get_twitter_avatar_img_url(candidate.twitter_url)
        if(current_img_url != candidate.picture_url):
            candidate.picture_url = current_img_url
            #TODO, candidate.updated_at = datetime.dateime.now()
            db.session.add(candidate)
            updates.append(candidate.last_name)
            print("{0} {1} picture_url WAS UPDATED! ".format(candidate.id, candidate.first_name))

    if(updates):
        db.session.commit()
        output_string = "Updated picture_url for {0} candidate(s). they were... ".format(len(updates))
        for update in updates:
            output_string = output_string + "  " + update + ","
        return(output_string)
    else:
        return("I checked for updates, but there were none.")

@app.route('/methods')
def methods():
    return render_template('methods.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')


if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)