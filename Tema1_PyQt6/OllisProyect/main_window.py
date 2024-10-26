# Librerias que he utilizado:
import sys 
import hashlib
import json # Libreria json para poder guardar los datos del formulario al registrarnos que tambien servirá para poder llamar a nuestro formulario a la hora de iniciar sesión
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCalendarWidget, QMessageBox # Libreria PyQt6 para poder desarrollar las interfaces mediante estos widgets
from PyQt6.QtCore import Qt

class window_login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OllisProyect - Login")

        self.traducciones = {
            "Español": {
                "title": "Iniciar Sesión",
                "name": "Introduce tu nombre",
                "password": "Introduce tu contraseña",
                "login": "Iniciar sesión",
                "cancel": "Cancelar",
                "language": "Idioma"
            },
            "Inglés": {
                "title": "Login",
                "name": "Enter your name",
                "password": "Enter your password",
                "login": "Log in",
                "cancel": "Cancel",
                "language": "Language"
            }
        }

        self.idioma_actual = "Español"

        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_login = QVBoxLayout()
        layout_btn_accept_exit = QHBoxLayout()
        layout_lenguage = QHBoxLayout()
        

        self.label_title = QLabel(self.traducciones[self.idioma_actual]["title"])
        fuente = self.label_title.font()
        fuente.setPointSize(20)
        self.label_title.setFont(fuente)
        layout_title.addWidget(self.label_title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)


        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText(self.traducciones[self.idioma_actual]["name"])
        layout_login.addWidget(self.lineEdit_name)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText(self.traducciones[self.idioma_actual]["password"])
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout_login.addWidget(self.lineEdit_password)

        layout_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.btn_accept = QPushButton(self.traducciones[self.idioma_actual]["login"])
        self.btn_accept.setFixedSize(100, 30)
        self.btn_accept.clicked.connect(self.iniciar_sesion)
        layout_btn_accept_exit.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(self.traducciones[self.idioma_actual]["cancel"])
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.clicked.connect(self.close)
        layout_btn_accept_exit.addWidget(self.btn_cancel)
        
        layout_btn_accept_exit.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.label_lenguage = QLabel(self.traducciones[self.idioma_actual]["language"])
        layout_lenguage.addWidget(self.label_lenguage)


        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "Inglés"])
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)


        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_login)
        layout_main.addLayout(layout_btn_accept_exit)
        layout_main.addLayout(layout_lenguage)


        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)
    
    def cambiar_idioma(self):
        self.idioma_actual = self.lenguage.currentText()

        self.label_title.setText(self.traducciones[self.idioma_actual]["title"])
        self.lineEdit_name.setPlaceholderText(self.traducciones[self.idioma_actual]["name"])
        self.lineEdit_password.setPlaceholderText(self.traducciones[self.idioma_actual]["password"])
        self.btn_accept.setText(self.traducciones[self.idioma_actual]["login"])
        self.btn_cancel.setText(self.traducciones[self.idioma_actual]["cancel"])
        self.label_lenguage.setText(self.traducciones[self.idioma_actual]["language"])

    
    def iniciar_sesion(self):
        name = self.lineEdit_name.text().strip()
        password = self.lineEdit_password.text().strip()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            with open("datos_formulario.json", "r") as archivo_json:
                datos = json.load(archivo_json)
                if datos["name"] == name and datos["password"] == hashed_password:
                    QMessageBox.information(self, "Success", "Login successful!")
                else:
                    QMessageBox.warning(self, "Error", "Invalid username or password.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No users registered yet")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error ocurred: {e}")
        


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
        self.btn_accept.clicked.connect(self.validar_campos_vacios)
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
        

    def guardar_formulario(self):
        password = self.lineEdit_password.text().strip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        datos_formulario = {
            "name": self.lineEdit_name.text(),
            "last_name": self.lineEdit_lastName.text(),
            "password": hashed_password,
            "email": self.lineEdit_email.text()
        }

        try:
            # Intentamos abrir el archivo en modo de lectura para cargar cuentas existentes
            with open("datos_formulario.json", "r") as archivo_json:
                try:
                    cuentas = json.load(archivo_json)  # Cargar cuentas si el JSON es válido
                except json.JSONDecodeError:
                    cuentas = []  # Si el JSON está vacío o es inválido, iniciamos una lista vacía
        except FileNotFoundError:
            cuentas = []  # Si el archivo no existe, iniciamos una lista vacía

        # Añadimos la nueva cuenta
        cuentas.append(datos_formulario)

        try:
            # Guardamos todas las cuentas en el archivo JSON
            with open("datos_formulario.json", "w") as archivo_json:
                json.dump(cuentas, archivo_json, indent=4)

            QMessageBox.information(self, "Information", "The form has been created successfully")

        except Exception as e:
            self.mostrar_error(f"Error saving JSON file: {e}")                
    
    def validar_campos_vacios(self):
        if not self.validar_campos_name_lastName(self.lineEdit_name.text().strip()):
            self.mostrar_error("The 'name' field must have at least one capital letter, three letters and contain no numbers.")
        elif not self.validar_campos_name_lastName(self.lineEdit_lastName.text().strip()):
            self.mostrar_error("The 'last name' field must have at least one capital letter, three letters and contain no numbers.")
        elif not self.validar_campo_password(self.lineEdit_password.text().strip()):
            self.mostrar_error("The 'password' field must have a minimum of 8 characters")
        elif not self.validar_campo_email(self.lineEdit_email.text().strip()):
            self.mostrar_error("The 'email' field must have @gmail or @hotmail")
        else:
           self.guardar_formulario()

    def validar_campos_name_lastName(self, field):
        if len(field) < 3:
            return False
        if not re.match(r'^[A-Za-z]+$', field):
            return False
        if not any(c.isupper() for c in field):
            return False
        return True
    
    def validar_campo_password(self, field):
        return len(field) >= 8
    
    def validar_campo_email(self, field):
        patron = r'^[a-zA-Z0-9._%-]+@(gmail|hotmail)\.com$'
        return re.match(patron, field) is not None

    def mostrar_error(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)


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
        self.btn_login.clicked.connect(self.window_login)
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

    def window_login(self):
        self.another_window2 = window_login()
        self.another_window2.show()



if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec()