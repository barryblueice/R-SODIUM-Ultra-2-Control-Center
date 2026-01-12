from PySide6.QtCore import Qt

class WidgetDrag:
    def __init__(self, window, topbar):
        self.window = window
        self.topbar = topbar
        self._drag_active = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.topbar.underMouse():
            self._drag_active = True
            self._drag_position = (
                event.globalPosition().toPoint()
                - self.window.frameGeometry().topLeft()
            )
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_active and event.buttons() & Qt.LeftButton:
            self.window.move(
                event.globalPosition().toPoint() - self._drag_position
            )
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_active = False
        event.accept()
