from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT Application")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("images/logo.png"))
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.create_line_edit()

    def create_line_edit(self):
        lineEdit = QLineEdit(self)
        lineEdit.setGeometry(180, 50, 200, 30)
        lineEdit.setPlaceholderText("Please enter your username")

        lineEdit.setFont(QFont("Arial", 12))            # <-- Then set font (important!)
        lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid #ffffff;
            }
        """)

        #self.setFocus()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
