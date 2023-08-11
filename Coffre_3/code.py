from clavier_matriciel import *


class Code:
    def __init__(self):
        self.clavier = Clavier()
        self.clavier.setup_gpio()
        self.code = "1234"
        self.pressed_keys = []

    def run(self):
        while True:
            pressed_key = self.clavier.detect_key()
            if pressed_key:
                if pressed_key == "F":
                    if "".join(self.pressed_keys) == self.code:
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
        self.clavier.cleanup()
