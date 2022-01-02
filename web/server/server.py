from flask import Flask, request, jsonify, render_template, session, redirect, url_for, g
from flask_cors import CORS

import json

import application_web
import users


app = Flask(__name__)
app.secret_key = 'secretkey'
CORS(app)

registered_users = users.registered_users

@app.before_request
def before_request():
    if 'username' in session:
        g.username = session['username']
    else:
        g.username = None

@app.route("/", methods=['GET', 'POST'])
def home():

    msg = request.json

    if (msg == None):
        return "Invalid Request"

    elif ("type" not in msg):
        return "Invalid Request"

    else:
        request_type = str(msg["type"])

        """find solutions"""
        if (request_type == "find_solutions"):
            traceback = str(msg["error"])
            code = str(msg["code"])
            number_of_solutions = str(msg["number_of_solutions"])
            result = application_web.main(_traceback=traceback, _code=code, _colored=False,  _n_answers=number_of_solutions)
            return result

        """upvote - downvote"""
        if ((request_type == "upvote") or (request_type == "downvote")):
            error_type = str(msg["error_type"])
            link = str(msg["link"])
            value = msg["value"]
            code = str(msg["code"])
            error = str(msg["error"])
            ip = str(msg["user_ip"])
            application_web.send_updownvote(link, error_type, value, code , error, ip);
            return  { "successful": [1] }

        else:
            return "Invalid Request"

@app.route("/login/", methods=['GET', 'POST'])
def login():

    session.pop('username', None)

    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        if (username in registered_users):
            if (registered_users[username] == password):
                session['username'] = username
                return redirect(url_for('votes'))
            else:
                return redirect(url_for('login'))
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/votes/")
def votes():

    if not g.username:
        return redirect(url_for('login'))


    file = open("/home/AriaAbrishamdar/mysite/vote/updowndata.json")
    solutions = json.load(file)

    return render_template('votes.html', solutions=solutions)


if __name__ == '__main__':
    app.run()
