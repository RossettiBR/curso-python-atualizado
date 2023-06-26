from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN, MINIMUM_HEIGHT
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils import isEmpty


class Display(QLineEdit):
    eqRequested = Signal()
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(MINIMUM_HEIGHT)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            print(f'EQ {text} pressionado, sinal emitido', type(self).__name__)
            self.eqRequested.emit()
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            print(f'isDelete {text} pressionado, sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()

        if isEsc:
            print('isEsc pressionado, sinal em,itido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        print('Texto', text)
