import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.despegable = QComboBox() # QComboBox: crear un despegable
        self.setCentralWidget(self.despegable)

        self.despegable.addItems(["Opción 1", "Opción 2", "Opción 3"]) # Array
        self.despegable.currentIndexChanged.connect(self.mostrar_indice) 
        self.despegable.currentTextChanged.connect(self.mostrar_texto)
    
    """
     def mostrar_texto(self):
        print(self.despegable.currentText())

    def mostrar_indice(self):
        print(self.despegable.currentText())
    """
    def mostrar_texto(self,t):
        print("--->", t)
    
    def mostrar_indice(self,s):
        print(s)
   

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


