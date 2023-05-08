""" WSB FLASK TEST """

from flask import Flask
app = Flask (__name__)

@app.route('/')
def index():
    """ Printing header with greetings from Flask """
    return '<h1>Hellow WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
