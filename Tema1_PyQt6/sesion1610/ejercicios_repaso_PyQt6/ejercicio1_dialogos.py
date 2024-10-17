import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Pulsa el botón")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
       QMessageBox.about(self, "Mensaje", "Hola")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


''' Build de QMessageBox()'''

'''
QMessageBox.about(parent, title, message) -> mensaje
QMessageBox.critical(parent, title, message) -> error
QMessageBox.information(parent, title, message) -> información
QMessageBox.question(parent, title, message) -> pregunta
QMessageBox.warning(parent, title, message) -> aviso

'''