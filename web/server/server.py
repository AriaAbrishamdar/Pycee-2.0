from flask import Flask, request, jsonify
from flask_cors import CORS

import usage_web


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    """Request in server"""
    traceback = str(request.json["error"])
    code = str(request.json["code"])
    result = usage_web.main(_traceback=traceback, _code=code, _colored=False)
    return result

if __name__ == '__main__':
    app.run()
