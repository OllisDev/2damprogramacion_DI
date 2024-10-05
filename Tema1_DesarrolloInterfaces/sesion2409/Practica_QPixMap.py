import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel, QApplication, QMainWindow)
from PyQt6.QtGui import (QPalette, QColor, QPixmap)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Main Window")
        label = QLabel("Hola")
        pixmap = QPixmap("Gato2.jpg") #QPixelMap: insertar una imagen
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(),pixmap.height())
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
        