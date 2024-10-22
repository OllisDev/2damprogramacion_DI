import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Crear layout vertical
        vbox = QVBoxLayout()
        
        # Crear botones y añadirlos al layout vertical
        btn1 = QPushButton("Botón Arriba")
        btn2 = QPushButton("Botón Abajo")
        vbox.addWidget(btn1)
        
        # Crear layout horizontal y añadir botones
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("Izquierda"))
        hbox.addWidget(QPushButton("Centro"))
        hbox.addWidget(QPushButton("Derecha"))
        
        # Añadir el layout horizontal al layout vertical
        vbox.addLayout(hbox)
        vbox.addWidget(btn2)
        
        # Asignar el layout a la ventana
        self.setLayout(vbox)
        self.setWindowTitle("Layout Mixto")
        self.setGeometry(100, 100, 400, 200)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


