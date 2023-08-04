import machine
import time

# Configuration des broches RX et TX
RX_PIN = 16  # Remplace par le numéro de broche que tu as connecté comme RX
TX_PIN = 17  # Remplace par le numéro de broche que tu as connecté comme TX

# Initialisation de la communication série
fingerprint_serial = machine.UART(2, baudrate=9600, rx=RX_PIN, tx=TX_PIN)


# Fonction pour traiter les données reçues
def process_data(data):
    print("Données reçues depuis le module :", data)
    # Traite les données reçues du module ici


def main():
    while True:
        if fingerprint_serial.any():
            data = fingerprint_serial.read(1)
            process_data(data)
        time.sleep_ms(100)  # Attend un peu avant de vérifier à nouveau


if __name__ == "__main__":
    main()
