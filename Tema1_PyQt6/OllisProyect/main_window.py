import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCalendarWidget
from PyQt6.QtCore import Qt

class window_register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OllisProyect - Register")

        self.traduccion = {
            "Español": {
                "title": "REGISTRO",
                "name": "Introduce tu nombre",
                "lastName": "Introduce tus apellidos",
                "password": "Introduce una contraseña",
                "email": "Introduce tu correo electrónico",
                "accept": "Aceptar",
                "exit": "Salir",
                "lenguage": "Idioma"
            },
            "English": {
                "title": "REGISTER",
                "name": "Enter your name",
                "lastName": "Enter your last name",
                "password": "Enter a password",
                "email": "Enter your email",
                "accept": "Accept",
                "exit": "Exit",
                "lenguage": "Lenguage"
            }
        }

        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_btn_accept_exit = QHBoxLayout()
        layout_form = QVBoxLayout()
        layout_form_container = QHBoxLayout()
        layout_lenguage = QHBoxLayout()

        self.title = QLabel(self.traduccion["Español"]["title"])
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuente = self.title.font()
        fuente.setPointSize(20)
        self.title.setFont(fuente)
        layout_title.addWidget(self.title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText(self.traduccion["Español"]["name"])
        layout_form.addWidget(self.lineEdit_name)
        
        self.lineEdit_lastName = QLineEdit()
        self.lineEdit_lastName.setPlaceholderText(self.traduccion["Español"]["lastName"])
        layout_form.addWidget(self.lineEdit_lastName)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText(self.traduccion["Español"]["password"])
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout_form.addWidget(self.lineEdit_password)

        self.lineEdit_email = QLineEdit()
        self.lineEdit_email.setPlaceholderText(self.traduccion["Español"]["email"])
        layout_form.addWidget(self.lineEdit_email)

        layout_form_container.addLayout(layout_form)
        layout_form_container.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.btn_accept = QPushButton(self.traduccion["Español"]["accept"])
        self.btn_accept.setFixedSize(100, 30)
        layout_btn_accept_exit.addWidget(self.btn_accept)

        self.btn_exit = QPushButton(self.traduccion["Español"]["exit"])
        self.btn_exit.setFixedSize(100, 30)
        self.btn_exit.clicked.connect(self.close)
        layout_btn_accept_exit.addWidget(self.btn_exit)

        layout_btn_accept_exit.setAlignment(Qt.AlignmentFlag.AlignRight)


        self.label_lenguage = QLabel(self.traduccion["Español"]["lenguage"])
        layout_lenguage.addWidget(self.label_lenguage)

        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "English"])
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)

        layout_lenguage.setAlignment(Qt.AlignmentFlag.AlignLeft)


        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_form_container)
        layout_main.addLayout(layout_btn_accept_exit)
        layout_main.addLayout(layout_lenguage)
        

        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)


    def cambiar_idioma(self):
        idioma = self.lenguage.currentText()

        self.title.setText(self.traduccion[idioma]["title"])
        self.lineEdit_name.setPlaceholderText(self.traduccion[idioma]["name"])
        self.lineEdit_lastName.setPlaceholderText(self.traduccion[idioma]["lastName"])
        self.lineEdit_password.setPlaceholderText(self.traduccion[idioma]["password"])
        self.lineEdit_email.setPlaceholderText(self.traduccion[idioma]["email"])
        self.btn_accept.setText(self.traduccion[idioma]["accept"])
        self.btn_exit.setText(self.traduccion[idioma]["exit"])
        self.label_lenguage.setText(self.traduccion[idioma]["lenguage"])

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
        self.btn_register.clicked.connect(self.window_register)
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

    def window_register(self):
        self.another_window1 = window_register()
        self.another_window1.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec()