from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication

class WidgetAni:
    @staticmethod
    def fade_in(widget):
        widget._fade_in_anim = QPropertyAnimation(widget, b"windowOpacity")
        anim = widget._fade_in_anim
        anim.setDuration(150)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()
        
    @staticmethod
    def fade_out_close(widget):
        widget._fade_out_anim = QPropertyAnimation(widget, b"windowOpacity")
        anim = widget._fade_out_anim
        anim.setDuration(150)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.finished.connect(QApplication.quit)
        anim.start()
        
    @staticmethod
    def minimize_window(widget):
        widget._mini_anim = QPropertyAnimation(widget, b"windowOpacity")
        anim = widget._mini_anim
        anim.setDuration(150)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        def on_finished():
            widget.showMinimized()
            widget.setWindowOpacity(1.0)
        
        anim.finished.connect(on_finished)
        anim.start()