from flask import Flask, request, jsonify
from flask_cors import CORS

import application_web


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():

    type = str(request.json["type"])

    """find solutions"""
    if (type == "find_solutions"):
        traceback = str(request.json["error"])
        code = str(request.json["code"])
        result = application_web.main(_traceback=traceback, _code=code, _colored=False)
        return result

    """upvote - downvote"""
    if ((type == "upvote") or (type == "downvote")):
        error_type = str(request.json["error_type"])
        link = str(request.json["link"])
        value = request.json["value"]
        application_web.send_updownvote(link, error_type, value);
        return  { "successful": [value] }


if __name__ == '__main__':
    app.run()
