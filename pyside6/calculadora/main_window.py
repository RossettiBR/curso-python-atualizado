from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurando o layout basico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # titulo
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # ultima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
