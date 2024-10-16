import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QHBoxLayout()

        b1 = QPushButton()
        b1.setText("Botón A")
    

        b2 = QPushButton()
        b2.setText("Botón B")

        b3 = QPushButton()
        b3.setText("Botón C")

        layout.addWidget(b1)
        layout.addSpacing(20) # addSpacing(): espacio entre componentes por pixeles

        layout.addWidget(b2)
        layout.addSpacing(20)

        layout.addWidget(b3)
        layout.addSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()