from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT Application")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("images/logo.png"))
        self.setFixedHeight(400)
        self.setFixedWidth(600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.setWindowOpacity(0.7)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())