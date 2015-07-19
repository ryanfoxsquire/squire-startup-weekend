import os
from flask import Flask, render_template
from flask import request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from settings import APP_STATIC
import csv
import json
from pdb import set_trace as pause
import requests
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
import operator
import os
import requests
import re
import nltk
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

email_addresses = []

@app.route('/')
@app.route('/index')
def hello_world():
    candidates = Candidate.query.order_by(Candidate.smi.desc()).all()
    return render_template('index.html', rankings_list = candidates)

@app.route('/refresh_data')
def refresh_data():
    candidates = Candidate.query.all()
    for candidate in candidates:
        current_img_url = get_twitter_avatar_img_url(candidate.twitter_url)
        updates = []
        if(current_img_url != candidate.picture_url):
            candidate.picture_url = current_img_url
            db.session.add(candidate)
            updates.append(candidate.last_name)
            print("{0} {1} picture_url WAS UPDATED! ".format(candidate.id, candidate.first_name))

    if(updates):
        db.session.commit()
        output_string = "Updated picture_url for {0} candidate(s). they were... ".format(len(updates))
        for update in updates:
            output_string = output_string + "  " + update
        return(output_string)
    else:
        return("I checked for updates, but there were none.")

@app.route('/fill_in_database')
def fill_in_database():

    # NOTE: THIS FUNCTION IS DEFUCNT NOW THAT csv has also been deleted from codebase. 
    # TO GET THIS FUNCTIONALITY BACK GO TO  COMMIT  https://github.com/ryanfoxsquire/squire-startup-weekend/commit/af6d307ac76864dfdee940fcc3bd30610ed24160
    # I used this function to fill in my initialize the content of my database. 
    regenerate_database_from_csv = False 

    if regenerate_database_from_csv:

      # build rankings list
        rankings_list = []
        with open(os.path.join(APP_STATIC, 'POTUS_Candidates_data.csv')) as f:
            reader = csv.DictReader(f)        
            for rows in reader:
                rows['full_name'] = rows['First'] + " " + rows['Last']
                rankings_list.append(rows) # each element is a dictionary
        
        for candidate in rankings_list:
            print("\n\n\n")
            print(candidate)    

            new_candidate_data = {'first_name' : candidate["First"],
                              'last_name' :candidate["Last"],
                              'party' : candidate["Party"].upper(),
                              'picture_url': candidate["picture_URL"],
                              'twitter_url': candidate["Twitter_URL"],
                              'facebook_url': candidate["FB_URL"],
                              'created_at': datetime.datetime.now(),
                              'updated_at': None,
                              'smi': str(candidate["SMI_Index_per_million"])
                              }
            new_candidate = Candidate(new_candidate_data)
            db.session.add(new_candidate)
        db.session.commit()
        return("SUCCESS! you loaded the database!")
    else:
        return( " set 'regenerate_database_from_csv = True' if you want to load files from the csv")

@app.route('/methods')
def methods():
    return render_template('methods.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/realpythontutorial_index', methods=['GET', 'POST'])
def realpythontutorial_index():
    # from https://realpython.com/blog/python/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/

    errors = []
    results = {}
    if request.method == "POST":
        print("POST RECEIVED\n\n")
        # get url that the person has entered
        try:
            url = request.form['url']
            print("\n")
            print(url)

            r = requests.get(url)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('realpythontutorial_index.html', errors=errors)
        if r:
            print("detected the url!!")

            # text processing
            raw = BeautifulSoup(r.text).get_text()
            nltk.data.path.append('./nltk_data/')  # set the path
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)

            # remove punctuation, count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)

            # stop words
            no_stop_words = [w for w in raw_words if w.lower() not in stops]
            no_stop_words_count = Counter(no_stop_words)

            # save the results
            results = sorted(
                no_stop_words_count.items(),
                key=operator.itemgetter(1),
                reverse=True
            )[0:10]
            try:
                result = Result(
                    url=url,
                    result_all=raw_word_count,
                    result_no_stop_words=no_stop_words_count
                )
                db.session.add(result)
                db.session.commit()
                print("saved {0} to db!".format(url))
            except:
                errors.append("Unable to add item to database.")
    print("rendering template...")
    return render_template('realpythontutorial_index.html', errors=errors, results=results)

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)