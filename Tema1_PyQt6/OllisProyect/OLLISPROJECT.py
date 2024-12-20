# Librerias que he utilizado:
import sys 
import hashlib
import json # Libreria json para poder guardar los datos del formulario al registrarnos que tambien servirá para poder llamar a nuestro formulario a la hora de iniciar sesión
import re # Libreria re para poder restringir algunos datos del formularios mediante los caracteres especiales
import subprocess # Libreria para poder iniciar un proceso despues de iniciar sesion y abrir un notepad
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCalendarWidget, QMessageBox # Libreria PyQt6 para poder desarrollar las interfaces mediante estos widgets
from PyQt6.QtCore import Qt


class window_login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OllisProyect - Login")


        self.traducciones = { # Guardamos en una variable todas las traducciones de español e ingles para poder intercambiar el idioma
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

        self.idioma_actual = "Español" # El idioma por defecto estará en español

        # Layouts
        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_login = QVBoxLayout()
        layout_btn_accept_exit = QHBoxLayout()
        layout_lenguage = QHBoxLayout()
        
        # Layout del titulo
        self.label_title = QLabel(self.traducciones[self.idioma_actual]["title"])
        fuente = self.label_title.font()
        fuente.setPointSize(20) # Cambiamos el tamaño de la letra
        self.label_title.setFont(fuente)
        layout_title.addWidget(self.label_title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter) # Lo alineamos para que se coloque tanto arriba del todo de la ventana como en el centro


        # Campos del nombre y contraseña
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText(self.traducciones[self.idioma_actual]["name"])
        layout_login.addWidget(self.lineEdit_name)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText(self.traducciones[self.idioma_actual]["password"])
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password) # Ocultar los caracteres del campo de la contraseña
        layout_login.addWidget(self.lineEdit_password)

        layout_login.setAlignment(Qt.AlignmentFlag.AlignCenter) # Alineamos el layout de inciar sesion en el centro de la ventana
        
        # Botón de aceptar y cancelar
        self.btn_accept = QPushButton(self.traducciones[self.idioma_actual]["login"])
        self.btn_accept.setFixedSize(100, 30)
        self.btn_accept.clicked.connect(self.iniciar_sesion) 
        layout_btn_accept_exit.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(self.traducciones[self.idioma_actual]["cancel"])
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.clicked.connect(self.close) # Cuando pulsemos el boton Cancelar se cierra la ventana
        layout_btn_accept_exit.addWidget(self.btn_cancel)
        
        layout_btn_accept_exit.setAlignment(Qt.AlignmentFlag.AlignRight) # Alineamos el layout de los botones a la derecha de la ventana

        self.label_lenguage = QLabel(self.traducciones[self.idioma_actual]["language"])
        layout_lenguage.addWidget(self.label_lenguage)

        # Selección de idioma
        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "Inglés"]) # El desplegable cuenta con dos idiomas: Español e Inglés
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)


        # Añadir los layouts al layout principal
        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_login)
        layout_main.addLayout(layout_btn_accept_exit)
        layout_main.addLayout(layout_lenguage)

        # Configurar el layout principal mediante el QWidget (centrar el layout en el centro de la pantalla)
        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)
    
    # Funcion cambiar_idioma(): cambiar idioma según que idioma eligas mediante el desplegable (QComboBox)
    def cambiar_idioma(self):
        self.idioma_actual = self.lenguage.currentText()

        # Cambiar textos según el idioma seleccionado
        self.label_title.setText(self.traducciones[self.idioma_actual]["title"])
        self.lineEdit_name.setPlaceholderText(self.traducciones[self.idioma_actual]["name"])
        self.lineEdit_password.setPlaceholderText(self.traducciones[self.idioma_actual]["password"])
        self.btn_accept.setText(self.traducciones[self.idioma_actual]["login"])
        self.btn_cancel.setText(self.traducciones[self.idioma_actual]["cancel"])
        self.label_lenguage.setText(self.traducciones[self.idioma_actual]["language"])

    # Función iniciar_sesion(): validar usuario y contraseña con el archivo JSON
    def iniciar_sesion(self):
        name = self.lineEdit_name.text().strip()
        password = self.lineEdit_password.text().strip()

        hashed_password = hashlib.sha256(password.encode()).hexdigest() # Hash criptografico para poder cifrar la contraseña al guardarlo en el archivo JSON

        try:
            # Cargar datos desde el archivo JSON
            with open("datos_formulario.json", "r") as archivo_json:
                datos = json.load(archivo_json)
                usuario_encontrado = False
                if isinstance(datos, list):
                    for cuenta in datos:
                        # Validamos si el usuario y la contraseña coinciden
                        if cuenta["name"] == name and cuenta["password"] == hashed_password:
                            usuario_encontrado = True
                            QMessageBox.information(self, "Success", "Login successful!")
                            self.abrir_aplicacion()
                            return
                    
                    if not usuario_encontrado:
                        QMessageBox.warning(self, "Error", "Invalid username or password.")

        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No users registered yet")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error ocurred: {e}")

    # Funcion abrir_aplicacion(): abrir Notepad al iniciar sesión correctamente
    def abrir_aplicacion(self):
        try:
            subprocess.Popen(["notepad"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not open application: {str(e)}")
        


class window_register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OllisProyect - Register")

        self.traduccion = { # Guardamos en una variable todas las traducciones de español e ingles para poder intercambiar el idioma
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

        # Layouts  
        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_btn_accept_exit = QHBoxLayout()
        layout_form = QVBoxLayout()
        layout_form_container = QHBoxLayout()
        layout_lenguage = QHBoxLayout()

        # Layout del título
        self.title = QLabel(self.traduccion["Español"]["title"])
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuente = self.title.font()
        fuente.setPointSize(20)
        self.title.setFont(fuente)
        layout_title.addWidget(self.title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter) # Alineamos el layout del titulo en el centro y arriba de la ventana

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
        layout_form_container.setAlignment(Qt.AlignmentFlag.AlignCenter) # Alineamos el layout que contiene el formulario en el centro de la ventana


        self.btn_accept = QPushButton(self.traduccion["Español"]["accept"])
        self.btn_accept.setFixedSize(100, 30)
        self.btn_accept.clicked.connect(self.validar_campos_vacios) # Al pulsar el botón de aceptar validará si el formulario se ha hecho de manera correcta
        layout_btn_accept_exit.addWidget(self.btn_accept)

        self.btn_exit = QPushButton(self.traduccion["Español"]["exit"])
        self.btn_exit.setFixedSize(100, 30)
        self.btn_exit.clicked.connect(self.close)
        layout_btn_accept_exit.addWidget(self.btn_exit)

        layout_btn_accept_exit.setAlignment(Qt.AlignmentFlag.AlignRight) # Alineamos el layout de los botones a la izquierda de la ventana


        self.label_lenguage = QLabel(self.traduccion["Español"]["lenguage"])
        layout_lenguage.addWidget(self.label_lenguage)

        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "English"])
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)

        layout_lenguage.setAlignment(Qt.AlignmentFlag.AlignLeft) # Alineamos el layout del desplegable a la izquierda de la ventana

        # Añadimos todos los layouts al layout principal
        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_form_container)
        layout_main.addLayout(layout_btn_accept_exit)
        layout_main.addLayout(layout_lenguage)
        
        # Configuración del layout principal
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
        
    # Función guardar_formulario(): guardamos cada creacion de un "usuario" del formulario en un archivo JSON 
    def guardar_formulario(self):
        password = self.lineEdit_password.text().strip() # Obtener el texto de la contraseña, eliminando los espacios en blanco
        hashed_password = hashlib.sha256(password.encode()).hexdigest() # Cifrar contraseña mediante la conversión de un texto a una cadena hexodecimal
        datos_formulario = { # Creamos todos los datos del formulario para poder obtener todos los campos del formulario
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
    
    # Función validar_campos_vacios(): comprobar si los campos del formulario no tenga espacios blancos o no estan rellenos. A parte de que los campos de contraseña e email tiene restricciones como tener un minimo de 8 caracteres o el email necesita tener el @gmail o @hotmail
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

    # Función validar campos_name_lastName(): comprueba si el campo del nombre y del apellido tenga al menos 3 caracteres, que solo tenga letras y que contenga al menos una letra mayúscula
    def validar_campos_name_lastName(self, field):
        if len(field) < 3:
            return False
        if not re.match(r'^[A-Za-z]+$', field):
            return False
        if not any(c.isupper() for c in field):
            return False
        return True
    
    # Función validar campo_password(): compureba si el campo de la contraseña tiene al menos 8 caracteres
    def validar_campo_password(self, field):
        return len(field) >= 8

    # Función validar_campo_email(): comprueba si el campo email contiene un @gmail o un @hotmail mediante la utilización de patrones de expresiones regulares
    def validar_campo_email(self, field): 
        patron = r'^[a-zA-Z0-9._%-]+@(gmail|hotmail)\.com$'
        return re.match(patron, field) is not None
    
    # Función mostrar_error(): mostrar un mensaje de error en caso de que no se cumpla las condiciones del formulario
    def mostrar_error(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)


class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setWindowTitle("OllisProject")

        self.traduccion = { # Guardamos en una variable todas las traducciones de español e ingles para poder intercambiar el idioma
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
        
        # Layouts
        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_btn_register_login =  QVBoxLayout()
        layout_btn_exit = QHBoxLayout()
        layout_lenguage = QHBoxLayout()

        # Configuración del layout del título
        self.title = QLabel("¡BIENVENIDO!")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter) # Alineamos el titulo en el centro de la ventana
        fuente = self.title.font()
        fuente.setPointSize(20) # Cambiamos el tamaño de la letra
        self.title.setFont(fuente)
        layout_title.addWidget(self.title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter) # Alineamos el layout del titulo al centro y arriba de la ventana
        
        # Colocamos el layout de los botones a la derecha mediante la utilización de espaciadores para empujarlos a la derecha
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout_btn_register_login.addItem(spacer_top)

        self.btn_register = QPushButton(self.traduccion[self.current_language]["register"])
        self.btn_register.setFixedSize(100, 30)
        self.btn_register.clicked.connect(self.window_register) # Cuando pulsemos el boton de Registrarse nos abra la ventana del Registro
        layout_btn_register_login.addWidget(self.btn_register)
        layout_btn_register_login.setAlignment(self.btn_register, Qt.AlignmentFlag.AlignHCenter) # Alineamos el layout de los botones en el centro de la ventana
        
        
        self.btn_login = QPushButton(self.traduccion[self.current_language]["login"])
        self.btn_login.setFixedSize(100,30)
        self.btn_login.clicked.connect(self.window_login) # Cuando pulsemos el botón de Iniciar Sesión nos abrirá la ventana de Iniciar Sesión
        layout_btn_register_login.addWidget(self.btn_login)
        layout_btn_register_login.setAlignment(self.btn_login, Qt.AlignmentFlag.AlignHCenter) 

        layout_btn_register_login.addItem(spacer_bottom) # Añadimos el espaciador al layout de los botones
        

        self.txt_lenguage = QLabel(self.traduccion[self.current_language]["language"])
        layout_lenguage.addWidget(self.txt_lenguage)

        self.lenguage = QComboBox()
        self.lenguage.addItems(["Español", "English"]) # El desplegable cuenta con dos idiomas: Español e Inglés
        self.lenguage.currentIndexChanged.connect(self.cambiar_idioma)
        layout_lenguage.addWidget(self.lenguage)
        
        
        spacer_exit = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout_btn_exit.addItem(spacer_exit)

        self.btn_exit = QPushButton(self.traduccion[self.current_language]["exit"])
        self.btn_exit.clicked.connect(self.close)
        layout_btn_exit.addWidget(self.btn_exit)

        # Añadir los layouts al layout principal
        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_btn_register_login)
        layout_main.addLayout(layout_btn_exit)
        layout_main.addLayout(layout_lenguage)

        spacer_lenguage = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        layout_lenguage.addItem(spacer_lenguage)

        # Configuracion del layout principal
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

    # Función window_register(): abrir la ventana del registro
    def window_register(self):
        self.another_window1 = window_register()
        self.another_window1.show()

    # Función window_login(): abrir la ventana de Iniciar Sesión
    def window_login(self):
        self.another_window2 = window_login()
        self.another_window2.show()


# Ejecutar la aplicacion
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec()