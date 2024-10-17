import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()

        label = QLabel()
        label.setText("Mi app")

        b1 = QPushButton()
        b1.setText("Botón 1")

        b2 = QPushButton()
        b2.setText("Botón 2")

        b3 = QPushButton()
        b3.setText("Botón 3")

        layout1.addWidget(label)
        layout2.addWidget(b1)
        layout2.addWidget(b2)
        layout2.addWidget(b3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        layout1.addLayout(layout2) # Añadir un layout a otro layout para poder combinar ambos
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()