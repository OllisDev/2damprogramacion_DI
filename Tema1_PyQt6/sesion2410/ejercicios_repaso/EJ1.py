import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv) # sys.argv(): lista de todos los argumentos de linea de comandos que pasamos cuando ejecutamos el códgio
    window = MainWindow()
    window.show()
    app.exec()