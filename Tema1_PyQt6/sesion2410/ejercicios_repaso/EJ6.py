import sys
from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QPushButton, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 400, 300)

        layout_main = QHBoxLayout()

        btn = QPushButton("Abrir Diálogo")
        btn.clicked.connect(self.button_clicked)
        layout_main.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    
    def button_clicked(self):
        dlg = QDialog()
        dlg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()