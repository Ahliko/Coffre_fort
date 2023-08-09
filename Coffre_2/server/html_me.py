from airium import Airium
import random as rd


class HTML:
    def __init__(self):
        self.a = Airium()
        self.note = []

    def html(self, connect):
        self.a('<!DOCTYPE html>')
        with self.a.html(lang="en"):
            with self.a.head():
                self.a.meta(charset="utf-8")
                self.a.title(_t="Coffre 2")
                self.a.link(rel="stylesheet", href="static/style.css")
            with self.a.body():
                if not connect:
                    self.a.h1(_t="Vous n'êtes pas connecté ! Veuillez vous connectez.")
                    with self.a.form(action="/verify", method="POST"):
                        self.a.input(type="text", name="username", placeholder="Username")
                        self.creatediv(self.a, self.random())
                        self.a.input(type="hidden", class_="note", name="note", value="0")
                        self.a.input(type="submit", value="Submit", onclick="check()")
                else:
                    self.a.h1("Vous êtes connecté !")
                    with self.a.form(action="/move", method="POST"):
                        self.a.input(type="submit", name="open", value="Open")
                        self.a.input(type="submit", name="close", value="Close")
                with self.a.script():
                    self.a("""let note = [];
                    
                    function notes(number) {
        note.push(number);
        console.log(note);
    }

    function check() {
        console.log(note);
        console.log(note.length);
        if (note.length === 4) {
            let noteString = note.join("");
            console.log(noteString);
            document.getElementsByClassName("note")[0].value = noteString;
        } else {
            document.getElementsByClassName("note")[0].value = "0";
        }
        note = [];
    }""")
        return str(self.a)

    @staticmethod
    def random(lst=None):
        if lst is None:
            lst = []
        i = 0
        while i < 10:
            rdm = rd.randint(0, 9)
            if rdm not in lst:
                lst.append(rdm)
                i += 1
        return lst

    @staticmethod
    def creatediv(a, lst):
        with a.div(class_="wrapper"):
            for i in lst:
                if i == 0:
                    number = "zero"
                elif i == 1:
                    number = "one"
                elif i == 2:
                    number = "two"
                elif i == 3:
                    number = "three"
                elif i == 4:
                    number = "four"
                elif i == 5:
                    number = "five"
                elif i == 6:
                    number = "six"
                elif i == 7:
                    number = "seven"
                elif i == 8:
                    number = "eight"
                elif i == 9:
                    number = "nine"
                with a.div(class_=f"{number}", onclick=f"notes({i})"):
                    a(i)
        return a

    def notes(self, note):
        self.note.append(note)

    def check(self):
        print(self.note)
        if len(self.note) == 0 or self.note is None:
            self.a.input(class_="note", type="hidden", name="note", value="0")
        else:
            self.a.input(class_="note", type="hidden", name="note", value=str(self.note))
        self.note = []
