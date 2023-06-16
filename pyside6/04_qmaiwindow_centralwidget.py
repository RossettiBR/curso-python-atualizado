import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QBoxLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

button_1 = QPushButton('Button 1')
button_1.setStyleSheet('font-size: 40px; color: red;')

button_2 = QPushButton('Button 2')
button_2.setStyleSheet('font-size: 40px; color: blue')

button_3 = QPushButton('Button 3')
button_3.setStyleSheet('font-size: 40px; color: green;')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button_1, 1, 1, 1, 1)
layout.addWidget(button_2, 1, 2, 1, 1)
layout.addWidget(button_3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(
    lambda: slot_example(status_bar)
)

# central_widget.show()
window.show()
app.exec()
