import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")

        layout_btn = QGridLayout()

        btn1 = QPushButton("Botón 1")
        layout_btn.addWidget(btn1, 0, 0)

        btn2 = QPushButton("Botón 2")
        layout_btn.addWidget(btn2, 0, 1)

        btn3 = QPushButton("Botón 3")
        layout_btn.addWidget(btn3,1, 0)

        btn4 = QPushButton("Botón 4")
        layout_btn.addWidget(btn4, 1, 1)

        widget = QWidget()
        widget.setLayout(layout_btn)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
