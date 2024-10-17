import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QLineEdit, QPushButton, QLabel)

class login (QWidget):
    def __init__(self):
        super().__init__()

    
        self.setWindowTitle("login ejemplo")
        self.setGeometry (600, 100, 300 ,300)

        layout = QGridLayout()

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Pon tu login aquí")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Pon tu contraseña aquí")
        layout.addWidget(self.nombre, 0, 1, 1, 2)
        layout.addWidget(self.password, 1, 1, 1, 2)

        nombreLabel = QLabel("Login")
        passwordLabel = QLabel("Password")
        layout.addWidget(nombreLabel, 0, 0)
        layout.addWidget(passwordLabel, 1, 0)
        
        btnLogin = QPushButton("Login")
        btnCancel = QPushButton("Cancel")
        layout.addWidget(btnLogin, 2, 0)
        layout.addWidget(btnCancel, 2, 1)
        
        btnCancel.clicked.connect(self.close) # Cerrar ventana mediante el boton Cancel

        btnLogin.clicked.connect(self.Inicio)
        self.setLayout(layout)


    def Inicio(self):
        try:
            if self.nombre.text() != "" and self.password.text() != "":
                print(self.nombre.text(), self.password.text())
            else:
                print("Error. Introduce datos.")
        except Exception as e: 
            print(e)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo_login = login()
    dialogo_login.show()
    sys.exit(app.exec())
