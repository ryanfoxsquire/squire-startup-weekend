from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

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
    app.run()