import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QPushButton
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        button = QPushButton()
        button.setText("Haz click")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("")
        dlg.exec()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()