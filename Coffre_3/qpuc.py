from clavier_matriciel import *
from RPLCD.gpio import CharLCD


class QPUC:
    def __init__(self):
        self.questions = [(1, "Quelle est la capitale de la France ?", "Paris", "Lyon", "Marseille", "Bordeaux", 1),
                          (2, "Dans la Saga Star Wars, quelle est la planète natale de Dark Vador ?", "Tatooine",
                           "Coruscant",
                           "Naboo", "Mustafar", 1),
                          (3, "Dans la Saga Star Wars, quel est le personnage appelé Space Jesus par les fans ?",
                           "Luke Skywalker",
                           "Obi-Wan Kenobi", "Anakin Skywalker", "Yoda", 2),
                          (4,
                           "Dans la Saga Star Wars, quel est le nom de l'ordre, lancé par Dark Sidious, qui a pour but d'éliminer \
                           les jedis ?",
                           "L'ordre 35", "Le Dernier Ordre", "L'ordre 66", "L'ordre 42", 3), ]

        self.clavier = Clavier()
        self.clavier.setup_gpio()

        self.lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

    def run(self):
        self.lcd.write_string("Bienvenue à Question Pour Un Coffre !")
        time.sleep(2)
        self.lcd.clear()
        self.lcd.write_string("Appuyez sur une touche pour commencer")
        while True:
            pressed_key = self.clavier.detect_key()
            if pressed_key:
                self.lcd.clear()
                break
            time.sleep(0.1)
        for question in self.questions:
            self.lcd.clear()
            self.lcd.write_string(question[1])
            time.sleep(2)
            self.lcd.clear()
            self.lcd.write_string("1: " + question[2])
            self.lcd.cursor_pos = (1, 0)
            self.lcd.write_string("2: " + question[3])
            time.sleep(2)
            self.lcd.clear()
            self.lcd.write_string("3: " + question[4])
            self.lcd.cursor_pos = (1, 0)
            self.lcd.write_string("4: " + question[5])
            time.sleep(2)
            self.lcd.clear()
            self.lcd.write_string("Votre réponse ?")
            while True:
                pressed_key = self.clavier.detect_key()
                if pressed_key:
                    self.lcd.clear()
                    break
                time.sleep(0.1)
            if pressed_key == str(question[6]):
                self.lcd.write_string("Bonne réponse !")
                time.sleep(2)
                self.lcd.clear()
                return True
            self.lcd.write_string("Mauvaise réponse !")
            time.sleep(2)
            self.lcd.clear()
            return False

    def cleanup(self):
        self.clavier.cleanup()
        self.lcd.clear()
        self.lcd.close(clear=True)
