import flask
from flask import Flask, render_template, redirect, request
import sqlite3
from html_me import HTML

app = Flask(__name__)


class User:
    def __init__(self):
        self.connect = False


theuser = User()


def check_user(username, password):
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Users')
    users = c.fetchall()
    for user in users:
        if user[1] == username and user[2] == password:
            return True
    return False


@app.route('/')
def index():
    h = HTML()
    return h.html(theuser.connect)


@app.route('/verify', methods=['POST'])
def verify():
    print(request.form['username'], request.form['note'])
    if check_user(request.form['username'], request.form['note']):
        theuser.connect = True
        print('User connected')
    else:
        theuser.connect = False
        print('User not connected')
    return redirect('/')


@app.route('/move', methods=['POST'])
def move():
    print()
    if request.form.get('open') == 'Submit':
        # TODO: Open the door
        print('Open')
    elif request.form.get('close') == 'Submit':
        # TODO: Close the door
        print('Close')
    elif request.form.get('destroy') == 'Submit':
        # TODO: Destroy the data of the Coffre
        print('Destroy')
    return redirect('/')


@app.route('/disconect', methods=['POST'])
def disconect():
    theuser.connect = False
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
