import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        label1 = QLabel()
        label1.setText("Etiqueta 1")
        layout.addWidget(label1)

        label2 = QLabel()
        label1.setText("Etiqueta 2")
        layout.addWidget(label2)

        label3 = QLabel()
        label3.setText("Etiqueta 3")
        layout.addWidget(label3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()