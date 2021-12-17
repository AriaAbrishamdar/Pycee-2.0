from flask import Flask, request, jsonify
from flask_cors import CORS

import application_web


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():

    msg = request.json

    if (msg == None):
        return { "successful": [0] }

    elif ("type" not in msg):
        return { "successful": [0] }

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
            application_web.send_updownvote(link, error_type, value);
            return  { "successful": [1] }

        else:
            return { "successful": [0] }


if __name__ == '__main__':
    app.run()
