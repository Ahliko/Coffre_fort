import RPi.GPIO as GPIO
import time

# Configuration des broches du clavier matriciel
ROWS = [5, 6, 13, 19]  # Broches connectées aux lignes
COLS = [12, 16, 20, 21]  # Broches connectées aux colonnes

# Matrice représentant les touches du clavier
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]


# Configuration initiale des broches GPIO
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for row in ROWS:
        GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for col in COLS:
        GPIO.setup(col, GPIO.OUT)
        GPIO.output(col, 1)


# Fonction pour détecter la touche pressée
def detect_key():
    key = None
    for col_num, col_pin in enumerate(COLS):
        GPIO.output(col_pin, 0)
        for row_num, row_pin in enumerate(ROWS):
            if not GPIO.input(row_pin):
                key = keys[row_num][col_num]
                while not GPIO.input(row_pin):
                    pass
        GPIO.output(col_pin, 1)
    return key


# Nettoyage des broches GPIO
def cleanup():
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        setup_gpio()
        while True:
            pressed_key = detect_key()
            if pressed_key:
                print("Touche pressée:", pressed_key)
            time.sleep(0.1)
    except KeyboardInterrupt:
        cleanup()
