import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        b1 = QPushButton()
        b1.setText("Botón 1")

        b2 = QPushButton()
        b2.setText("Botón 2")

        b3 = QPushButton()
        b3.setText("Botón 3")

        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(b3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()