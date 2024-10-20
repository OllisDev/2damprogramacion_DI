import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QComboBox
from PyQt6.QtCore import Qt
class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setWindowTitle("OllisProject")
        
        layout_main = QVBoxLayout()
        layout_title = QVBoxLayout()
        layout_btn_register_login =  QVBoxLayout()
        layout_btn_exit = QHBoxLayout()
        layout_lenguage = QHBoxLayout()

        title = QLabel("¡BIENVENIDO!")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fuente = title.font()
        fuente.setPointSize(20)
        title.setFont(fuente)
        layout_title.addWidget(title)
        layout_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout_btn_register_login.addItem(spacer_top)

        btn_register = QPushButton("Regístrate")
        btn_register.setFixedSize(100, 30)
        layout_btn_register_login.addWidget(btn_register)
        layout_btn_register_login.setAlignment(btn_register, Qt.AlignmentFlag.AlignHCenter)
        
        
        btn_login = QPushButton("Inicie sesión")
        btn_login.setFixedSize(100,30)
        layout_btn_register_login.addWidget(btn_login)
        layout_btn_register_login.setAlignment(btn_login, Qt.AlignmentFlag.AlignHCenter)

        layout_btn_register_login.addItem(spacer_bottom) 
        

        txt_lenguage = QLabel("Idioma")
        layout_lenguage.addWidget(txt_lenguage)

        lenguage = QComboBox()
        lenguage.addItems(["Español", "English"])
        layout_lenguage.addWidget(lenguage)
        
        
        spacer_exit = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout_btn_exit.addItem(spacer_exit)

        btn_exit = QPushButton("Salir")
        layout_btn_exit.addWidget(btn_exit)

        layout_main.addLayout(layout_title)
        layout_main.addLayout(layout_btn_register_login)
        layout_main.addLayout(layout_btn_exit)
        layout_main.addLayout(layout_lenguage)

        spacer_lenguage = QSpacerItem(30, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        layout_lenguage.addItem(spacer_lenguage)

        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)

        
         

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec()