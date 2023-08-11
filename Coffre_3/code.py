from clavier_matriciel import *

clavier = Clavier()
clavier.setup_gpio()
code = "1234"

pressed_keys = []

while True:
    pressed_key = clavier.detect_key()
    if pressed_key:
        if pressed_key == "F":
            if "".join(pressed_keys) == code:
                print("Code correct !")
                break
            else:
                print("Code incorrect !")
                pressed_keys = []
        pressed_keys.append(pressed_key)
        print("Touche pressée:", pressed_key)
    time.sleep(0.1)