from flask import Flask, redirect, request
import sqlite3
from html_me import HTML
from check_code import TOTP


app = Flask(__name__)


class Server:
    def __init__(self):
        self.connect = False
        self.goa2f = False
        self.a2f = TOTP()


server = Server()


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
    return h.html_root(server.connect)


@app.route('/verify', methods=['POST'])
def verify():
    print(request.form['username'], request.form['note'])
    if not check_user(request.form['username'], request.form['note']):
        server.connect = False
        return redirect('/')
    server.goa2f = True
    return redirect('/a2f')


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
    server.connect = False
    return redirect('/')


@app.route("/a2f")
def a2f():
    if not server.goa2f:
        return redirect("/")
    h = HTML()
    return h.html_a2f()


@app.route("/a2f_check", methods=["POST"])
def a2f_check():
    if not server.goa2f:
        return redirect("/")
    if server.a2f.verify(request.form["a2f"]):
        server.connect = True
        server.goa2f = False
        return redirect("/")
    else:
        return redirect("/a2f")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
