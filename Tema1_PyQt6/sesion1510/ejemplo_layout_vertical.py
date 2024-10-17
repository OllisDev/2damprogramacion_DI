import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        layout = QVBoxLayout() # QVBoxLayout(): ordenar componentes de manera vertical

        botton = QPushButton() # QPushButton(): crear boton
        botton.setText("Aceptar") #setText(): ponerle un nombre al boton
        
        botton2 = QPushButton()
        botton2.setText("Cancelar")

        layout.addWidget(botton) #addWidget(): añadir componente
        layout.addWidget(botton2)

        widget = QWidget() # Crear el Qwidget para añadir layout y añadirlo al mainwindow
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()