import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QHBoxLayout() # QHBoxLayout(): ordenar componentes de manera horizontal

        botton = QPushButton()
        botton.setText("Aceptar")

        botton2 = QPushButton()
        botton2.setText("Cancelar")

        layout.addWidget(botton)
        layout.addWidget(botton2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()