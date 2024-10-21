#importamos las librerías necesarias
import sys
from PyQt6 import QtWidgets, uic

from PyQt6.QtWidgets import (QApplication, QDialog, QMainWindow, QPushButton, 
                             QVBoxLayout, QLabel, QDialogButtonBox, QMessageBox)

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("C:/Users/Iker/Documents/2DamProgramacion_DI-master/2damprogramacion_DI-1/Tema1_PyQt6/sesion1510/ejemplo2.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)
        self.mibtn.clicked.connect(self.funcion2)
        
    def funcion(self):
        print("ejemplo")

    def funcion2(self):
        msgBox = QMessageBox()
        msgBox.setText("Ejemplo de qt designer")
        msgBox.exec()


# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())