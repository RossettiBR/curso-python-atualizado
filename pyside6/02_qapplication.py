import sys
from PySide6.QtWidgets import QApplication,  QPushButton


app = QApplication(sys.argv)

button = QPushButton('Button')
button.setStyleSheet('font-size: 40px; color: red;')
button.show()

app.exec()
