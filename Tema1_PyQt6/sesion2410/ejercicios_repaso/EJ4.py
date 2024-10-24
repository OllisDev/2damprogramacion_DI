import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicacion")
        self.setGeometry(100, 100, 400, 300)

        layout_main = QHBoxLayout()

        self.lineEdit = QLineEdit()
        layout_main.addWidget(self.lineEdit)

        btn = QPushButton("Mostrar")
        btn.clicked.connect(self.button_clicked)
        layout_main.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def button_clicked(self):
        mensaje = self.lineEdit.text()
        QMessageBox.information(self, "Texto ingresado", f"Has escrito: {mensaje}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()