import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 400, 300)

        layout_main = QHBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.comboBox.currentIndexChanged.connect(self.opcion)
        layout_main.addWidget(self.comboBox)

        self.opcion1 = QLabel("Selecciona una opción")
        layout_main.addWidget(self.opcion1)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def opcion(self):
        opcion2 = self.comboBox.currentText()
        self.opcion1.setText(f"Has seleccionado: {opcion2}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()