import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
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
        dlg = QDialog()
        dlg.setWindowTitle("Título")
        button1 = QPushButton()
        button1.setText("Cerrar")
        button1.clicked.connect(dlg.accept)
        
        layout = QVBoxLayout() # Para poder añadir el botón al dialogo, necesitamos crear un layout, sino la máquina entederá que el botón se creará en la ventana principal (MainWindow)
        layout.addWidget(button1)
        dlg.setLayout(layout)

        dlg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()