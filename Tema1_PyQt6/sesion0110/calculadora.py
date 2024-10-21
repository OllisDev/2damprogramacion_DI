
import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton,QLineEdit,QGridLayout)

class calculadora(QWidget):

    def metodo1():
        pass

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LA calcula de la liga Fantasia")
        self.setGeometry (600,100,300,300)

        self.resultado = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.resultado,0,0,1,5)
        nombre_boton = [["1","2","3","+"],
                        ["4","5","6","-"],
                        ["7","8","9", "*"],
                        ["0","/",".","="]]
        # añadir componentes.
        for i in range (1,5):
            for j in range (4): 
                boton = QPushButton(nombre_boton[i-1][j])
                layout.addWidget(boton,i,j)
                boton.clicked.connect(self.press_button)

        self.setLayout(layout)

    def press_button (self):
        sender = self.sender()
        if (sender.text() == "=" ):
            try:
                
                self.resultado.setText(str(eval(self.resultado.text())))
            except (Exception):
                self.resultado.setText("operación inválida")
        else:
            self.resultado.setText(self.resultado.text() + sender.text())


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    calc = calculadora()
    calc.show()
    sys.exit(app.exec())