import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel, QApplication, QMainWindow
)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        widget = QLabel ("Hola, soy Iker") # QLabel: etiqueta
        font = widget.font()
        font.setPointSize(10) # setPointSize: cambiar tamaño de letra
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # Alinear etiqueta en el centro tanto horizontal como vertical

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

