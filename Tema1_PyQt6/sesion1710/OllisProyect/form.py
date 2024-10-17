import sys
from PyQt6 import QtWidgets, uic

from PyQt6.QtWidgets import (QApplication, QDialog, QMainWindow, QPushButton, 
                             QVBoxLayout, QLabel, QDialogButtonBox, QMessageBox, QHBoxLayout)


class Window(QtWidgets.QMainWindow):
    def __init__(self, padre=None):
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi("C:/Users/Iker/Documents/2DamProgramacion_DI-master/2damprogramacion_DI-1/Tema1_PyQt6/sesion1710/OllisProyect/Form.ui", self)
        self.setWindowTitle("Form")

        self.pushButton_2.clicked.connect(self)
        self.pushButton.clicked.connect(self)

        
