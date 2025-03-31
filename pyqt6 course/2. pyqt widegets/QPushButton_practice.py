from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize

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

    def create_button(self):
        btn = QPushButton("Click Here", self)
        btn.setStyleSheet("background-color: black; border-radius: 10px;")
        btn.setGeometry(180, 50, 200, 50)
        btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        btn.setIcon(QIcon("images/logo.png"))
        btn.setIconSize(QSize(40, 40))

        menu = QMenu()  
        menu.addAction("Option 1")
        menu.addAction("Option 2")
        menu.addAction("Option 3")
        btn.setMenu(menu)


app = QApplication(sys.argv)

window = Window()
window.create_button()
window.show()

sys.exit(app.exec())