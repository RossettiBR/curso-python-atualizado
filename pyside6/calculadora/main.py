import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICONS
from info import Info
from style import setupTheme
from buttons import Button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # define um icone
    icon = QIcon(str(WINDOW_ICONS))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    button = Button('Texto do botão')
    window.addToVLayout(button)

    # executa tudo
    window.adjustFixedSize()
    window.show()

    app.exec()
