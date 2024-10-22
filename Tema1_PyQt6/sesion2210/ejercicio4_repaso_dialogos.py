import sys
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow,QHBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")

        layout_main = QHBoxLayout()

        btn = QPushButton("Pulsame")
        btn.clicked.connect(self.btn_clicked)
        layout_main.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        

    def btn_clicked(self):
        dlg = QDialog()
        dlg.setWindowTitle("My dialog")
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

        