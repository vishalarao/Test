from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''Simple function'''
    return "Hello World"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5151, debug=False)
    
