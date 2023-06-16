import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Button')
button.setStyleSheet('font-size: 40px; color: red;')

button_2 = QPushButton('Button Two')
button_2.setStyleSheet('font-size: 60px; color: blue;')

central_widget = QWidget()
layout = QGridLayout()
layout.addWidget(button, 1, 2)
layout.addWidget(button_2, 1, 1)
central_widget.setLayout(layout)

central_widget.show()

app.exec()
