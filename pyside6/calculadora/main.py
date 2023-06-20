import sys

from buttons import Button, ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme
from variables import WINDOW_ICONS

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # define um icone
    icon = QIcon(str(WINDOW_ICONS))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    # executa tudo
    window.adjustFixedSize()
    window.show()

    app.exec()
