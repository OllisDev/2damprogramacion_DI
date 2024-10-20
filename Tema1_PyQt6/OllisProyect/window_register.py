import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor

class window_register(QMainWindow):

    def __init__(self):
        super(window_register, self).__init__()

        self.setWindowTitle("My App")

app = QApplication(sys.argv)
window = window_register()
window.show()

app.exec()