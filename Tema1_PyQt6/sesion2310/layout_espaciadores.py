import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")
        
        layout = QVBoxLayout()

        label = QLabel("Hola")
        layout.addWidget(label)

        layout.addStretch() # addStretch() = añadir un espacio entre varios layouts o widgets

        btn = QPushButton("Pulsame")
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()