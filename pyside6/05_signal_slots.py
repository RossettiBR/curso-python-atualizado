import sys
from PySide6.QtCore import Slot
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


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_action = primeiro_menu.addAction('Segunda ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)
segunda_action.hovered.connect(terceiro_slot(segunda_action))

button_1.clicked.connect(terceiro_slot(segunda_action))

# central_widget.show()
window.show()
app.exec()
