from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    """Request in server"""
    text = str(len(str(request.json["text"])))
    return text

if __name__ == '__main__':
    app.run()
