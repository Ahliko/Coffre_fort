import flask
from flask import Flask, render_template

app = Flask(__name__)


class Data:
    def __init__(self, name):
        self.name = name
        self.age = 20


@app.route('/')
def index():
    data = Data("John")
    return render_template(flask.url_for('index.html'), data=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/song')
def song():
    return app.redirect('/about')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
