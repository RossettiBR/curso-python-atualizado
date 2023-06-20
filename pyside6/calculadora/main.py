import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICONS
from info import Info

if __name__ == '__main__':
    app = QApplication()

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

    # executa tudo
    window.adjustFixedSize()
    window.show()

    app.exec()
