import machine
import random
import time


def set_memori():
    memori = []
    for i in range(0, 9):
        memori.append(random.randint(1, 4))
    return memori


class Memori:
    def __init__(self):
        self.memori = set_memori()
        self.led_jaune = machine.Pin(12, machine.Pin.OUT)
        self.led_bleu = machine.Pin(13, machine.Pin.OUT)
        self.led_rouge = machine.Pin(14, machine.Pin.OUT)
        self.led_verte = machine.Pin(15, machine.Pin.OUT)
        self.button_a = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_b = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_c = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_d = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
        self.led_jaune.value(False)
        self.led_bleu.value(False)
        self.led_rouge.value(False)
        self.led_verte.value(False)

    def get_memori(self):
        return self.memori

    def run(self):
        for i in self.get_memori():
            if i == 1:
                self.led_jaune.value(True)
                time.sleep(1)
                self.led_jaune.value(False)
                time.sleep(1)
            elif i == 2:
                self.led_bleu.value(True)
                time.sleep(1)
                self.led_bleu.value(False)
                time.sleep(1)
            elif i == 3:
                self.led_rouge.value(True)
                time.sleep(1)
                self.led_rouge.value(False)
                time.sleep(1)
            elif i == 4:
                self.led_verte.value(True)
                time.sleep(1)
                self.led_verte.value(False)
                time.sleep(1)
            else:
                raise "Erreur : Valeur inconnue"
        for i in range(0, 9):
            if self.button_a.value():
                button_pressed = 1
            elif self.button_b.value():
                button_pressed = 2
            elif self.button_c.value():
                button_pressed = 3
            elif self.button_d.value():
                button_pressed = 4
            else:
                i += 1
                continue
            if not button_pressed == self.get_memori()[i]:
                return False
        return True
