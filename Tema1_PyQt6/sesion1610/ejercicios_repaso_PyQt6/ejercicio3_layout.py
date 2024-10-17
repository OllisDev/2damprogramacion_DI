import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout = QGridLayout()

        b1 = QPushButton()
        b1.setText("1")

        b2 = QPushButton()
        b2.setText("2")

        b3 = QPushButton()
        b3.setText("3")

        b4 = QPushButton()
        b4.setText("4")

        layout.addWidget(b1, 0,0)
        layout.addWidget(b2, 0,1)
        layout.addWidget(b3, 1,0)
        layout.addWidget(b4, 1,1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()