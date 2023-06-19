# import sys
from PySide6.QtWidgets import QApplication, QLabel

from main_window import MainWindow


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()

    q_label = QLabel('O meu texto')
    q_label.setStyleSheet('font-size: 40px; color: red;')
    window.v_layout.addWidget(q_label)
    window.adjustFixedSize()
    window.show()

    app.exec()
