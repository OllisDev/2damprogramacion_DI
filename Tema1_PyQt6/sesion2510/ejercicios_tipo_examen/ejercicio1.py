from PyQt6.QtWidgets import (
    QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox, QLabel, QVBoxLayout
)
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
import sys

class RegistroForm(QWidget):
    def __init__(self):
        super().__init__()
        
        # Crear el layout principal
        layout = QVBoxLayout()

        # Crear el layout del formulario
        self.form_layout = QFormLayout()

        # Campos de entrada
        self.nombre = QLineEdit()
        self.apellidos = QLineEdit()
        self.correo = QLineEdit()
        self.contrasena = QLineEdit()
        self.confirmar_contrasena = QLineEdit()

        # Configurar QLineEdit para ocultar el texto de las contraseñas
        self.contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmar_contrasena.setEchoMode(QLineEdit.EchoMode.Password)

        # Validación de correo
        correo_regex = QRegularExpression(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        correo_validator = QRegularExpressionValidator(correo_regex)
        self.correo.setValidator(correo_validator)

        # Agregar campos al layout del formulario
        self.form_layout.addRow("Nombre:", self.nombre)
        self.form_layout.addRow("Apellidos:", self.apellidos)
        self.form_layout.addRow("Correo Electrónico:", self.correo)
        self.form_layout.addRow("Contraseña:", self.contrasena)
        self.form_layout.addRow("Confirmar Contraseña:", self.confirmar_contrasena)

        # Botones de registrar y cancelar
        self.boton_registrar = QPushButton("Registrar")
        self.boton_registrar.clicked.connect(self.validar_formulario)
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_cancelar.clicked.connect(self.close)
        
        # Agregar los botones al layout
        layout.addLayout(self.form_layout)
        layout.addWidget(self.boton_registrar)
        layout.addWidget(self.boton_cancelar)

        # Configurar la ventana principal
        self.setLayout(layout)
        self.setWindowTitle("Formulario de Registro")

    def validar_formulario(self):
        # Verificar campos vacíos
        if not self.nombre.text() or not self.apellidos.text() or not self.correo.text() or not self.contrasena.text() or not self.confirmar_contrasena.text():
            QMessageBox.warning(self, "Error", "Por favor, completa todos los campos.")
            return

        # Verificar que el correo sea válido
        if not self.correo.hasAcceptableInput():
            QMessageBox.warning(self, "Error", "Por favor, ingresa un correo válido.")
            return

        # Verificar que las contraseñas coincidan
        if self.contrasena.text() != self.confirmar_contrasena.text():
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        # Si todos los campos son válidos
        QMessageBox.information(self, "Registro Exitoso", "Registro completado correctamente.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroForm()
    ventana.show()
    sys.exit(app.exec())
