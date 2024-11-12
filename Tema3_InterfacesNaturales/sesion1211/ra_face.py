import cv2
import numpy as np


# Cargar los clasificadores preentrenados de OpenCV para rostros y sonrisas
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Cargar la imagen del emoji (asegúrate de tener un archivo "smile.png")
emoji = cv2.imread('C:\Users\Iker\Downloads\smile.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar si el archivo de emoji se cargó correctamente
if emoji is None:
    print("Error: No se pudo cargar el archivo 'smile.jpg'. Verifica la ruta.")
    exit()

# Iniciar la cámara
cap = cv2.VideoCapture(0)



while True:
    # Capturar un frame de video
    ret, frame = cap.read()

    # Convertir el frame a escala de grises (necesario para la detección)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

    # Para cada rostro detectado
    for (x, y, w, h) in faces:
        
        # Región de interés (ROI) en escala de grises para la sonrisa (dentro del rostro detectado)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detectar sonrisas en el rostro detectado
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        # Si se detecta al menos una sonrisa
        if len(smiles) > 0:
            # Redimensionar el emoji al tamaño del rostro
            emoji_resized = cv2.resize(emoji, (w, h))

            # Crear una máscara para el emoji
            alpha_s = emoji_resized[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            # Superponer el emoji en el rostro
            for c in range(0, 3):
                roi_color[:, :, c] = (alpha_s * emoji_resized[:, :, c] + alpha_l * roi_color[:, :, c])
            
    # Mostrar el frame resultante
    cv2.imshow('Detector de Sonrisas con emoji', frame)

    # Salir del loop si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
