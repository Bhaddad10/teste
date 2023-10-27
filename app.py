
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hi')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
