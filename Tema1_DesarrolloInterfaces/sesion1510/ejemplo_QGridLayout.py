import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QGridLayout() #QGridLayout(): ordenar componentes en forma de tabla

        b1 = QPushButton()
        b1.setText("Botón 1")

        b2 = QPushButton()
        b2.setText("Botón 2")

        b3 = QPushButton()
        b3.setText("Botón 3")

        b4 = QPushButton()
        b4.setText("Botón 4")

        layout.addWidget(b1, 0, 0, 1, 1) # (nombre boton, fila, columna, rowSpan, columnSpan)
        layout.addWidget(b2, 0, 1, 1, 1)
        layout.addWidget(b3, 0, 2, 1, 1)
        layout.addWidget(b4, 1, 0, 1, 3) # Expansión de tres columnas

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()