from flask import Flask, render_template, redirect, request
import sqlite3

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
    return render_template('index.html', data=theuser)


@app.route('/verify', methods=['POST'])
def verify():
    if check_user(request.form['username'], request.form['password']):
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
    else:
        # TODO: Close the door
        print('Close')
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
