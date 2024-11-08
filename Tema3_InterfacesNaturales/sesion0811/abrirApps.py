import cv2
import mediapipe as mp
import os
import time

# Inicializar el módulo de MediaPipe para detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Rutas a aplicaciones específicas para cada gesto
aplicaciones = {
    "puño": r"C:\Program Files\Google\Chrome\Application\chrome.exe",        # Aplicación para el gesto de puño
    "mano_abierta": r"C:\Riot Games\VALORANT\live\VALORANT.exe", # Aplicación para el gesto de mano abierta
    "tijera": r"C:\Program Files (x86)\Steam\steam.exe"          # Aplicación para el gesto de tijera
}

# Función para detectar el gesto de la mano
def detectar_gesto(mano_landmarks):
    dedos_abiertos = []
    for i in [8, 12, 16, 20]:  # Índices de las yemas de los dedos (índice, medio, anular, meñique)
        if mano_landmarks.landmark[i].y < mano_landmarks.landmark[i - 2].y:  # Dedo está abierto
            dedos_abiertos.append(True)
        else:
            dedos_abiertos.append(False)
    
    if all(dedos_abiertos):
        return "mano_abierta"
    elif dedos_abiertos[0] and not any(dedos_abiertos[1:]):
        return "tijera"
    else:
        return "puño"

# Función para abrir una aplicación específica según el gesto
def abrir_aplicacion(gesto):
    if gesto in aplicaciones:
        aplicacion = aplicaciones[gesto]
        print(f"Abriendo {aplicacion} para el gesto '{gesto}'")
        os.startfile(aplicacion)  # Abre la aplicación en Windows
    else:
        print(f"No hay aplicación asignada para el gesto '{gesto}'")

# Iniciar captura de video
cap = cv2.VideoCapture(0)

print("Sistema de reconocimiento de gestos activo. Usa gestos para abrir aplicaciones.")
ultimo_gesto = None
ultimo_tiempo = time.time()

# Bucle principal de detección
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a RGB para MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = hands.process(frame_rgb)

    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            # Calcular área aproximada de la mano detectada
            area_mano = abs(hand_landmarks.landmark[0].x - hand_landmarks.landmark[9].x) * abs(hand_landmarks.landmark[0].y - hand_landmarks.landmark[9].y)
            
            # Verifica que el área sea suficientemente grande para evitar falsos positivos
            if area_mano > 0.01:
                # Detectar el gesto de la mano
                gesto = detectar_gesto(hand_landmarks)
                
                # Evita ejecutar varias veces en un intervalo corto
                tiempo_actual = time.time()
                if gesto != ultimo_gesto and (tiempo_actual - ultimo_tiempo) > 2:
                    print(f"Gesto detectado: {gesto}")
                    abrir_aplicacion(gesto)
                    ultimo_gesto = gesto
                    ultimo_tiempo = tiempo_actual

            # Dibujar las conexiones de la mano en la imagen
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar el video en una ventana
    cv2.imshow('Detector de Gestos para Abrir Aplicaciones', frame)

    # Salir al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
hands.close()
cv2.destroyAllWindows()
