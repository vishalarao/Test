from flask import Flask
import sys
import optparse
import time

app = Flask(__name__)
start = int(round(time.time()))

@app.route("/")
def hello_world():

    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5999, debug=False)
    #app.run(port=5000, debug=False)
