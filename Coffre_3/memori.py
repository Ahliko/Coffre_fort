import RPi.GPIO as GPIO
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
        GPIO.setmode(GPIO.BCM)
        self.led_jaune = 12
        self.led_bleu = 13
        self.led_rouge = 14
        self.led_verte = 15
        self.button_a = 0
        self.button_b = 1
        self.button_c = 2
        self.button_d = 3
        GPIO.setup(self.led_jaune, GPIO.OUT)
        GPIO.setup(self.led_bleu, GPIO.OUT)
        GPIO.setup(self.led_rouge, GPIO.OUT)
        GPIO.setup(self.led_verte, GPIO.OUT)
        GPIO.setup(self.button_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_c, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_d, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.led_jaune, False)
        GPIO.output(self.led_bleu, False)
        GPIO.output(self.led_rouge, False)
        GPIO.output(self.led_verte, False)

    def get_memori(self):
        return self.memori

    def run(self):
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
        for i in range(0, 9):
            button_pressed = None
            if GPIO.input(self.button_a) == GPIO.LOW:
                button_pressed = 1
            elif GPIO.input(self.button_b) == GPIO.LOW:
                button_pressed = 2
            elif GPIO.input(self.button_c) == GPIO.LOW:
                button_pressed = 3
            elif GPIO.input(self.button_d) == GPIO.LOW:
                button_pressed = 4
            else:
                continue
            if button_pressed is not None and button_pressed != self.get_memori()[i]:
                return False
        return True


# Clean up GPIO settings when done
def cleanup():
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        game = Memori()
        result = game.run()
        if result:
            print("Congratulations! You won!")
        else:
            print("Oops! You lost.")
    except KeyboardInterrupt:
        cleanup()
