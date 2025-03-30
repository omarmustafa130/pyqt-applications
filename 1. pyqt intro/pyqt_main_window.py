from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("PyQT  Application")
window.setWindowTitle("PyQT Application")
window.menuBar().addMenu("File")
window.show()

sys.exit(app.exec())