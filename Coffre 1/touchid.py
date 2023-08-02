import machine
import time

# Configuration du port UART - assurez-vous de configurer les bons paramètres pour votre module "3 click"
uart_port = machine.UART(1, baudrate=9600, rx=17,
                         tx=16)  # Exemple de configuration pour UART1 sur les broches 17 (RX) et 16 (TX)
uart_port.init(9600, bits=8, parity=None, stop=1)

# Commandes pour le module "3 click" - ces commandes peuvent varier selon le modèle
cmd_enroll = b'\xEF\x01'
cmd_verify = b'\xEF\x02'
cmd_identify = b'\xEF\x03'


def send_command(command):
    uart_port.write(command)
    time.sleep(0.1)  # Attendre une courte période pour laisser le module répondre
    response = uart_port.read(12)  # Lire la réponse de 12 octets du module
    return response


def enroll_fingerprint():
    print("Placez votre doigt sur le capteur pour l'enrôlement.")
    response = send_command(cmd_enroll)
    # Analyser la réponse du module pour déterminer si l'enrôlement a réussi
    # Vérifiez le format de la réponse dans la documentation du module.


def verify_fingerprint():
    print("Placez votre doigt sur le capteur pour vérifier l'empreinte.")
    response = send_command(cmd_verify)
    # Analyser la réponse du module pour déterminer si la vérification a réussi
    # Vérifiez le format de la réponse dans la documentation du module.


def identify_fingerprint():
    print("Placez votre doigt sur le capteur pour l'identification.")
    response = send_command(cmd_identify)
    # Analyser la réponse du module pour déterminer si l'identification a réussi
    # Vérifiez le format de la réponse dans la documentation du module.


if __name__ == "__main__":
    try:
        while True:
            # Exemple d'utilisation : Vous pouvez appeler la fonction correspondante en fonction de votre besoin
            # enroll_fingerprint()
            # verify_fingerprint()
            # identify_fingerprint()
            time.sleep(2)  # Attendre 2 secondes entre chaque opération
    except KeyboardInterrupt:
        print("Arrêt de l'application.")
