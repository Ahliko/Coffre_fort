import machine
from pyfingerprint import PyFingerprint
import time


def fingerprint_sensor():
    print("fonction")
    f = PyFingerprint(machine.UART(2,
                                   baudrate=115200,
                                   tx=17,
                                   rx=16),
                      address=0xFFFFFFFF,
                      password=0x00000000)
    # f.setSystemParameter(4, 12)
    print("init")
    print(f.verifyPassword())
    if not f.verifyPassword():
        raise ValueError('Le capteur d\'empreintes digitales ne peut pas être vérifié')
    while True:
        print("debut")
        print(f.readImage())
        if f.readImage():
            f.convertImage(0x01)
            result = f.searchTemplate()
            if result >= 0:
                print('Empreinte digitale reconnue')
            else:
                print('Empreinte digitale inconnue')
        time.sleep(1)


fingerprint_sensor()