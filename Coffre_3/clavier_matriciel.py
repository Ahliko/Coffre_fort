import RPi.GPIO as GPIO
import time


class Clavier:
    def __init__(self):
        self.ROWS = [5, 6, 13, 19]  # Broches connectées aux lignes
        self.COLS = [12, 16, 20, 21]  # Broches connectées aux colonnes
        self.keys = [
            ['1', '2', '3', 'F'],
            ['4', '5', '6', 'E'],
            ['7', '8', '9', 'D'],
            ['A', '0', 'B', 'C']
        ]

    def setup_gpio(self):
        """Setup GPIO pins"""
        GPIO.setmode(GPIO.BCM)
        for row in self.ROWS:
            GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for col in self.COLS:
            GPIO.setup(col, GPIO.OUT)
            GPIO.output(col, 1)

    def detect_key(self):
        """Detect key press"""
        key = None
        for col_num, col_pin in enumerate(self.COLS):
            GPIO.output(col_pin, 0)
            for row_num, row_pin in enumerate(self.ROWS):
                if not GPIO.input(row_pin):
                    key = self.keys[row_num][col_num]
                    while not GPIO.input(row_pin):
                        pass
            GPIO.output(col_pin, 1)
        return key

    @staticmethod
    def cleanup():
        """Clean up GPIO pins"""
        GPIO.cleanup()

    def run(self):
        """Run the program"""
        try:
            self.setup_gpio()
            while True:
                pressed_key = self.detect_key()
                if pressed_key:
                    print("Touche pressée:", pressed_key)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.cleanup()
