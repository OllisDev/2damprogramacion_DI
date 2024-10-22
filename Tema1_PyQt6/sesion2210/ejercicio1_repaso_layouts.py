import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")

        layout_btn = QVBoxLayout()
        layout_main = QVBoxLayout()

        btn1 = QPushButton("Botón 1")
        layout_btn.addWidget(btn1)

        btn2 = QPushButton("Botón 2")
        layout_btn.addWidget(btn2)

        btn3 = QPushButton("Botón 3")
        layout_btn.addWidget(btn3)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

        layout_main.addLayout(layout_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
