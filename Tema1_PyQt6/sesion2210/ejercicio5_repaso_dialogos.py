import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QMessageBox, QLabel, QMainWindow

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmación")

        layout_main = QVBoxLayout()

        label = QLabel("¿Quieres continual?")
        layout_main.addWidget(label)
        
        btn_accept = QPushButton("Aceptar")
        layout_main.addWidget(btn_accept)

        btn_cancel = QPushButton("Cancelar")
        layout_main.addWidget(btn_cancel)

        btn_accept.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)

        self.setLayout(layout_main)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")

        btn = QPushButton("Pulsame", self)
        btn.clicked.connect(self.abrir_dialogo)

        self.setCentralWidget(btn)
    
    

    def abrir_dialogo(self):
        dialog = Dialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Resultado", "Aceptado")
        else :
            QMessageBox.warning(self, "Resultado", "Cancelado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()