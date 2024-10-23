import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QProgressBar, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My app")

        layout_main = QVBoxLayout()
        layout_fila1 = QHBoxLayout()
        layout_fila2 = QHBoxLayout()

        btn1 = QPushButton("Botón 1")
        layout_fila1.addWidget(btn1)

        btn2 = QPushButton("Botón 2")
        layout_fila1.addWidget(btn2)

        label = QLabel("Progreso")
        layout_fila2.addWidget(label)

        progressBar = QProgressBar()
        progressBar.setValue(100)
        progressBar.setRange(0, 100)
        layout_fila2.addWidget(progressBar)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        
        layout_main.addLayout(layout_fila1)
        layout_main.addLayout(layout_fila2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()