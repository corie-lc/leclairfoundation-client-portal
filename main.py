from flask import Flask
from flask import render_template
from helpers.systems import get_user_requests
from flask_session import Session
from flask import Flask, render_template, redirect, request, session, url_for

from helpers import systems

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = '681336'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

sess = Session()
sess.init_app(app)

Session(app)


def check_logged_redirect():
    if session.get('logged_in'):
        if session['logged_in'] != True:
            return False
        else:
            return True

    else:
        return False



@app.context_processor
def utility_processor():
  def requests(): 
      print("heres")     
      return systems.get_user_requests(session['username'])
  return dict(requests=requests)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_request', methods=['POST', 'GET'])
def create_request():
    systems.create_request(request.form.get('request_info'), session['username'])
    
    return redirect('/dashboard')

@app.route('/dashboard', methods=['POST', 'GET'])
def login_page():
    
    if check_logged_redirect():
        return render_template("dashboard.html")
    else:
    
        username = request.form.get('login-email')
        password = request.form.get('login-password')
        
        if systems.login(username, password) == True:
            session['username'] = username
            session['logged_in'] = True
            return render_template("dashboard.html")
        else:
            return render_template("index.html")

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
    


    