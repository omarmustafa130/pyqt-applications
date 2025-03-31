from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
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
        label = QLabel("Hello, PyQt!", self)
        #label.setText("NEW TEXT!")
        #label.move(100, 100)
        label.setFont(QFont("Sanserif", 20))
        label.setStyleSheet("color: #333;")
        label.setGeometry(230, 25, 200, 50)
        #label.setNum(12)
        #label.clear()
        label2 = QLabel(self)
        label2.setPixmap(QPixmap("images/logo.png"))
        label2.setScaledContents(True)
        label2.setGeometry(250, 100, 100, 100)


        label3 = QLabel(self)
        movie = QMovie("images/sky.gif")
        movie.setSpeed(500)
        label3.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())