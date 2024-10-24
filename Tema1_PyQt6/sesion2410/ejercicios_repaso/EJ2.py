import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 400, 300)

        layout_main = QHBoxLayout()

        btn = QPushButton("Cerrar")
        btn.clicked.connect(self.close) # close: cerrar ventana
        layout_main.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()