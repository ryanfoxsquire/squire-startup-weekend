import os
from flask import Flask, render_template
from flask import request, redirect
from settings import APP_STATIC
import csv
from pdb import set_trace as pause
app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():

    # build rankings list
    rankings_list = []
    with open(os.path.join(APP_STATIC, 'POTUS_Candidates_data.csv')) as f:
        reader = csv.DictReader(f)        
        for rows in reader:
            rows['full_name'] = rows['First'] + " " + rows['Last']
            rankings_list.append(rows) # each element is a dictionary

    return render_template('index.html', 
                            rankings = rankings_list[1], 
                            rankings_list = rankings_list,
                            loops = [1,2,3,4,5])

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("\nThe email address is '" + email + "'")
    email_addresses.append(email)
    print("Whole List: \n{0}".format(email_addresses))
    return redirect('/')

@app.route('/methods')
def methods():
    return render_template('methods.html')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)