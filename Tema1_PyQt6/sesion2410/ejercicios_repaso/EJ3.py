import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 400, 300)

        layout_main = QVBoxLayout()

        btn1 = QPushButton("Aceptar")
        layout_main.addWidget(btn1)
        btn2 = QPushButton("Cancelar")
        layout_main.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

