import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICONS

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()

    # define um icone
    icon = QIcon(str(WINDOW_ICONS))
    window.setWindowIcon(icon)

    # Display

    display = Display()
    window.addToVLayout(display)

    # executa tudo
    window.adjustFixedSize()
    window.show()

    app.exec()
