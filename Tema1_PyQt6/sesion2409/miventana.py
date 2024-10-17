import sys 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class miventana (QMainWindow): #Hereda de la clase QMainWindow
    def __init__(self): #Constructor (self: this en java)
        super().__init__()
        self.setWindowTitle("Mi ventana") #Nombre de la ventana
        button = QPushButton("Cliqueame") #Generar botón
        button.setCheckable(True) #Formato check
        button.clicked.connect(self.the_button_was_clicked) #Funcionalidad del botón que escribe por pantalla "me están clickeando"
        button.clicked.connect(self.the_button_was_toggled) #Funcionalidad del botón que detecta si se ha clickeado al botón con un booleano 
        self.setCentralWidget(button) #Cambiar la posición en el centro de la ventana
        
        
        
    
    def the_button_was_clicked(self): #Metodo que al presionar el boton me escriba por pantalla "me están clickeando"
        print ("me están clickeando") 
    
    def the_button_was_toggled(self, checked): #Método que al presionar el botón detecta si se ha clickeado al botón con un booleano (True/False)
         print ("Checked?", checked)  
         

app = QApplication(sys.argv) #Para coger argumentos
ventana = miventana()
ventana.show()
app.exec()
        