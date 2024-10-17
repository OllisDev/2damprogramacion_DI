#Importación del encolador de eventos (QApplication), ventana gráfica (QWidget) y un botón (QPushButton)
from PyQt6.QtWidgets import QApplication,QWidget, QPushButton, QMainWindow
import sys


app = QApplication(sys.argv) #Atributo app para invocar el encolador de eventos
ventana = QWidget() #Atributo ventana para la creación de ventana
main = QMainWindow() #Atributo main que genera la ventana generadora
boton = QPushButton("Botón Rojo") #Atributo boton para invocar un botón que se llama Boton Rojo
main.show() #Mostra ventana generadora
boton.show() #Mostrar boton
ventana.show() #Mostrar ventana
app.exec() #Ejecutar aplicación
