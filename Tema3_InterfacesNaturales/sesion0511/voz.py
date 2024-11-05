import speech_recognition as sr
import subprocess

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente de voz')
        audio = r.listen(source)
        

        try:
            audio = r.listen(source, phrase_time_limit=5)
            text = r.recognize_google(audio, language="es-ES")
            print('Has dicho {}'.format(text))
            print(text)

            if "hola" in text.lower():
                print("Abriendo Steam...")
                ruta_steam = r"C:\Program Files (x86)\Steam\Steam.exe"
                subprocess.Popen(f'start "" "{ruta_steam}"', shell=True)
            else:
                print("No se detectó un comando válido")

        except sr.UnknownValueError:
            print('No te he entendido')
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento de voz")
