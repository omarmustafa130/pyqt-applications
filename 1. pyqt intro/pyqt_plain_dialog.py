from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

window = QDialog()
window.setWindowTitle("PyQT Application")
window.show()

sys.exit(app.exec())