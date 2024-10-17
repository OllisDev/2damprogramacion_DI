#importamos las librerías necesarias
import sys
from PyQt6 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("C:/Users/Iker/Documents/2DamProgramacion_DI-master/2damprogramacion_DI/Tema1_DesarrolloInterfaces/sesion1110/ejercicio1.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.funcion)

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.funcion2)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        
        
        

    def funcion(self):
        if self.label.text() == "":
            self.label.setText("Hola clase")
        else:
            self.label.setText("")

    def funcion2(self):
        if self.label_2.text() == "":
            self.label_2.setText("Hola clase, que tal")
        else:
            self.label_2.setText("")

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())