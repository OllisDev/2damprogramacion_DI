import cv2
import speech_recognition as sr
import pyttsx3
import numpy as np
import threading

colores = {
    "rojo": (0, 0, 255),
    "verde": (0, 255, 0),
    "azul": (255, 0, 0),
    "amarillo": (0, 255, 255),
    "morado": (255, 0, 255),
    "cián": (255, 255, 0)
}

color_cubo = colores["verde"]
anunciado = False  # Para evitar que se anuncie más de una vez

# Inicializamos el motor de voz globalmente
engine = pyttsx3.init()


def decir_texto(texto):
    engine.say(texto)
    engine.runAndWait()

# Función para anunciar el color en un hilo separado
def anunciar_color(color_nombre):
    global anunciado
    if not anunciado:  # Solo anunciar si no se ha hecho antes
        print(f"Anunciado: El color del cubo es {color_nombre}")
        # Usar el motor de voz en el hilo principal
        threading.Thread(target=decir_texto, args=(f"El color del cubo es {color_nombre}",)).start()
        anunciado = True  # Marca que ya se ha anunciado

def abrir_camara_voz():
    global color_cubo

    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Di 'camara' o elige un color de tu cubo (azul, verde, cián, rojo, verde, morado o amarillo)")
            print("Escuchando...")

            try:
                audio = r.listen(source)
                comando = r.recognize_google(audio, language="es-ES")
                print(f"Comando detectado: {comando}")

                if comando.lower() == "cámara":
                    print("¡Abrir cámara!")
                    detectar_cubo()
                elif comando.lower() in colores:
                    color_cubo = colores[comando.lower()]
                    print(f"Color del cubo cambiado a: {comando.lower()}")
                elif comando.lower() == "salir":
                    print("Saliendo del programa.")
                    break
            except sr.UnknownValueError:
                print("No se encontró el comando. Inténtalo de nuevo.")
            except sr.RequestError as e:
                print(f"Error en el reconocimiento de voz: {e}")

def detectar_cubo():
    global color_cubo, anunciado
    
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    parameters = cv2.aruco.DetectorParameters()

    cap = cv2.VideoCapture(0)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    camera_matrix = np.array([[frame_width, 0, frame_width / 2],
                            [0, frame_height, frame_height / 2],
                            [0, 0, 1]], dtype="double")
    dist_coeffs = np.zeros((4, 1))

    axis = np.float32([[0, 0, 0], [0, 5, 0], [5, 5, 0], [5, 0, 0],
                    [0, 0, -5], [0, 5, -5], [5, 5, -5], [5, 0, -5]])

    def draw_cube(img, corners, imgpts, color):
        imgpts = np.int32(imgpts).reshape(-1, 2)
        img = cv2.drawContours(img, [imgpts[:4]], -1, color, 3)
        for i, j in zip(range(4), range(4, 8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), color, 3)
        img = cv2.drawContours(img, [imgpts[4:]], -1, color, 3)
        return img

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

        if np.all(ids is not None):  
            for corner in corners:
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corner, 5, camera_matrix, dist_coeffs)
                (rvec - tvec).any()

                cv2.aruco.drawDetectedMarkers(frame, corners)

                imgpts, _ = cv2.projectPoints(axis, rvec, tvec, camera_matrix, dist_coeffs)
                frame = draw_cube(frame, corner, imgpts, color_cubo)

                # Anunciar el color del cubo solo una vez
                color_nombre = obtener_nombre_color(color_cubo)
                if not anunciado:
                    anunciar_color(color_nombre)

        else:
            # Resetear anuncio si el cubo ya no está visible
            anunciado = False

        cv2.imshow('AR Cube', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def obtener_nombre_color(color):
    for nombre, valor in colores.items():
        if valor == color:
            return nombre

if __name__ == "__main__":
    abrir_camara_voz()
