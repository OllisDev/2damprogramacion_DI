import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked) # button.clicked.connect(): dar funcionalidad al pulsar el botón 
        button.setCheckable(True) # setCheckable(): comprueba con un booleano si el boton se pulsa
        self.setCentralWidget(button)

    def button_clicked(self, s): # Función que al hacer clic que imprima por pantalla un mensaje que ponga click + la señal
        print("click", s) # s (signal) -> enviar señal de que al pulsar el botón envia un false o un true 


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()