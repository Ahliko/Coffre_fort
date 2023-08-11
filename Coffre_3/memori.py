import RPi.GPIO as GPIO
import random
from clavier_matriciel import *


class Memori:
    def __init__(self):
        self.memori = []
        GPIO.setmode(GPIO.BCM)
        self.led_jaune = 12
        self.led_bleu = 13
        self.led_rouge = 14
        self.led_verte = 15
        self.clavier = Clavier()
        self.clavier.setup_gpio()
        GPIO.setup(self.led_jaune, GPIO.OUT)
        GPIO.setup(self.led_bleu, GPIO.OUT)
        GPIO.setup(self.led_rouge, GPIO.OUT)
        GPIO.setup(self.led_verte, GPIO.OUT)
        GPIO.output(self.led_jaune, False)
        GPIO.output(self.led_bleu, False)
        GPIO.output(self.led_rouge, False)
        GPIO.output(self.led_verte, False)
        self.pressed_keys = []

    def get_memori(self):
        return self.memori

    def set_memori(self):
        random.seed()
        self.memori = []
        for i in range(0, 9):
            self.memori.append(random.randint(1, 4))

    def show_memori(self):
        for i in self.get_memori():
            if i == 1:
                GPIO.output(self.led_jaune, True)
                time.sleep(1)
                GPIO.output(self.led_jaune, False)
                time.sleep(1)
            elif i == 2:
                GPIO.output(self.led_bleu, True)
                time.sleep(1)
                GPIO.output(self.led_bleu, False)
                time.sleep(1)
            elif i == 3:
                GPIO.output(self.led_rouge, True)
                time.sleep(1)
                GPIO.output(self.led_rouge, False)
                time.sleep(1)
            elif i == 4:
                GPIO.output(self.led_verte, True)
                time.sleep(1)
                GPIO.output(self.led_verte, False)
                time.sleep(1)
            else:
                raise ValueError("Erreur : Valeur inconnue")

    def run(self):
        while True:
            self.set_memori()
            self.show_memori()
            while True:
                pressed_key = self.clavier.detect_key()
                if pressed_key:
                    if pressed_key == "F":
                        if "".join(self.pressed_keys) == "".join([str(i) for i in self.memori]):
                            print("Code correct !")
                            return True
                        else:
                            print("Code incorrect !")
                            self.pressed_keys = []
                            return False
                    self.pressed_keys.append(pressed_key)
                    print("Touche pressée:", pressed_key)
                time.sleep(0.1)

    def cleanup(self):
        GPIO.cleanup()
        self.clavier.cleanup()


# Clean up GPIO settings when done


if __name__ == "__main__":
    game = Memori()
    try:
        result = game.run()
        if result:
            print("Congratulations! You won!")
        else:
            print("Oops! You lost.")
    except KeyboardInterrupt:
        game.cleanup()
