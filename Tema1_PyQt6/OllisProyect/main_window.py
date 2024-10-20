import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QComboBox
from PyQt6.QtCore import Qt
class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setWindowTitle("OllisProject")

        self.traduccion = { 
            "Español": {
                "title": "¡BIENVENIDO!",
                "register": "Regístrate",
                "login": "Inicie sesión",
                "language": "Idioma",
                "exit": "Salir"
            },
            "English": {
                "title": "WELCOME!",
                "register": "Register",
                "login": "Log in",
                "language": "Language",
                "exit": "Exit"
            }
        }

        self.current_language = "Español"
        
        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_btn_register_login =  QVBoxLayout()
        layout_btn_exit = QHBoxLayout()
        layout_lenguage = QHBoxLayout()

        self.title = QLabel("¡BIENVENIDO!")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuente = self.title.font()
        fuente.setPointSize(20)
        self.title.setFont(fuente)
        layout_title.addWidget(self.title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout_btn_register_login.addItem(spacer_top)

        self.btn_register = QPushButton(self.traduccion[self.current_language]["register"])
        self.btn_register.setFixedSize(100, 30)
        layout_btn_register_login.addWidget(self.btn_register)
        layout_btn_register_login.setAlignment(self.btn_register, Qt.AlignmentFlag.AlignHCenter)
        
        
        self.btn_login = QPushButton(self.traduccion[self.current_language]["login"])
        self.btn_login.setFixedSize(100,30)
        layout_btn_register_login.addWidget(self.btn_login)
        layout_btn_register_login.setAlignment(self.btn_login, Qt.AlignmentFlag.AlignHCenter)

        layout_btn_register_login.addItem(spacer_bottom) 
        

        self.txt_lenguage = QLabel(self.traduccion[self.current_language]["language"])
        layout_lenguage.addWidget(self.txt_lenguage)

        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "English"])
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)
        
        
        spacer_exit = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout_btn_exit.addItem(spacer_exit)

        self.btn_exit = QPushButton(self.traduccion[self.current_language]["exit"])
        self.btn_exit.clicked.connect(self.close)
        layout_btn_exit.addWidget(self.btn_exit)

        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_btn_register_login)
        layout_main.addLayout(layout_btn_exit)
        layout_main.addLayout(layout_lenguage)

        spacer_lenguage = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        layout_lenguage.addItem(spacer_lenguage)

        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)

    def cambiar_idioma(self):
        self.current_language = self.lenguage.currentText()

        self.title.setText(self.traduccion[self.current_language]["title"])
        self.btn_register.setText(self.traduccion[self.current_language]["register"])
        self.btn_login.setText(self.traduccion[self.current_language]["login"])
        self.txt_lenguage.setText(self.traduccion[self.current_language]["language"])
        self.btn_exit.setText(self.traduccion[self.current_language]["exit"])



if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec()