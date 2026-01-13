from PySide6.QtCore import QObject
from PySide6.QtCore import Signal as pyqtSignal
from PySide6.QtWidgets import QCheckBox

class FanCurveVisabilityController(QObject):
    switch_signal = pyqtSignal(int)

    def __init__(self, all_widgets=None):
        super().__init__()
        self.all_widgets = all_widgets or []

    def set_all_widgets(self, widgets):
        self.all_widgets = widgets
        cb: QCheckBox
        for index, cb in enumerate(self.all_widgets):
            cb.clicked.connect(lambda checked, i=index: self._handle_click(i))

    def _handle_click(self, index):
        self.switch_signal.emit(index)