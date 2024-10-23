import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMainWindow, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Formulario")

        layout_form = QFormLayout()

        layout_form.addRow("Nombre: ", QLineEdit())
        layout_form.addRow("Correo Electrónico: ", QLineEdit())
        layout_form.addRow("Contraseña: ", QLineEdit())
        layout_form.addRow(QPushButton("Enviar"))

        widget = QWidget()
        widget.setLayout(layout_form)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

        