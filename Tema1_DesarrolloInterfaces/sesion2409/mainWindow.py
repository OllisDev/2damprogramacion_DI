import sys 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.label = QLabel()
    
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
    
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
    
        container = QWidget()
        container.setLayout(layout)
    
        self.setCentralWidget(container)

app = QApplication(sys.argv) #Para coger argumentos
ventana = mainWindow()
ventana.show()
app.exec()
        
    