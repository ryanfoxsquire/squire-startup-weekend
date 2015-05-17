import os
from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    #author = "Me"
    #name = "You"
    rankings = { 
        'name' : 'Hillary Clinton',
        'alt' : 'Clinton_image',
        'rank_num' : str(1) + '. ', # as a string
        'image_url' : "https://pbs.twimg.com/profile_images/597758898087587840/WFulk7EO_400x400.png",
        'party' : '[D]',
        'SMI' : str(3.92)
        }

    return render_template('index.html', rankings = rankings, loops = [1,2,3,4,5])

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("\nThe email address is '" + email + "'")
    email_addresses.append(email)
    print("Whole List: \n{0}".format(email_addresses))
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)