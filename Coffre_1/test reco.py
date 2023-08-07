import cv2
import face_recognition

# Charger l'image pré-enregistrée (la personne que vous souhaitez reconnaître)
image_pre_enregistree = face_recognition.load_image_file("photos/0.JPG")
encodage_image_pre_enregistree = face_recognition.face_encodings(image_pre_enregistree)[0]

# Initialiser la webcam
cap = cv2.VideoCapture(0)

# Créer la fenêtre pour l'affichage
cv2.namedWindow('Reconnaissance faciale en temps réel')

delai_fps = int(1000 / 60)

try:
    while True:
        # Capture une image depuis la webcam
        ret, frame = cap.read()

        # Trouver les visages dans l'image capturée
        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) > 0:
            encodage_visage_capture = face_recognition.face_encodings(frame, face_locations)[0]

            # Comparer l'encodage du visage capturé avec l'encodage de l'image pré-enregistrée
            resultat_comparaison = face_recognition.compare_faces([encodage_image_pre_enregistree],
                                                                  encodage_visage_capture)

            if resultat_comparaison[0]:
                cv2.putText(frame, "Correspondance", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Pas de correspondance", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Afficher l'image avec les résultats de la comparaison
        cv2.imshow('Reconnaissance faciale en temps réel', frame)

        keystroke = cv2.waitKey(20)  # Wait for Key press
        if keystroke == 27:
            break  # if key pressed is ESC then escape the loop

except KeyboardInterrupt:
    print("Interruption clavier")

finally:
    # Libérer la webcam et fermer la fenêtre OpenCV
    cap.release()
    cv2.destroyAllWindows()
