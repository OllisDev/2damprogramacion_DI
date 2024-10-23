import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QGridLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")

        layout_main = QGridLayout()

        label = QLabel("Hola")
        layout_main.addWidget(label, 0, 0)

        lineEdit = QLineEdit()
        layout_main.addWidget(lineEdit, 0, 1)

        pushButton = QPushButton("Pulsame")
        layout_main.addWidget(pushButton, 1, 0)

        checkBox = QCheckBox()
        checkBox.isChecked()
        layout_main.addWidget(checkBox, 1, 1)

        comboBox = QComboBox()
        comboBox.addItems(["Español", "English"])
        layout_main.addWidget(comboBox, 2, 0, 1, 2)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


