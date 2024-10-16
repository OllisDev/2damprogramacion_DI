import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow): # Clase MainWindow extiende de la clase QMainWindow (ventana visual)

    def __init__(self):
        super(MainWindow, self).__init__() # Constructor

        self.setWindowTitle("My App by iker ;)") # Titulo de la ventana

        widget = QWidget() # Crear el Qwidget para añadir layout y añadirlo al MainWindow
        self.setCentralWidget(widget)


app = QApplication(sys.argv) # QApplication(): hace que la aplicacion funcione
window = MainWindow()
window.show() # show(): mostrar ventana
app.exec() # exec(): ejecutar aplicacion