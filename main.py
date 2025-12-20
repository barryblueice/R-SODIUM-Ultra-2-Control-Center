import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from Ui_main import Ui_Dialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setWindowOpacity(0.0)
        self.show()
        self.fade_in()

        self.ui.close.clicked.connect(self.fade_out_close)
        self.ui.minimize.clicked.connect(self.minimize_window)
            
    def fade_in(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(300)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()
        self.fade_in_anim = anim
        
    def fade_out_close(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(300)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.finished.connect(QApplication.quit)
        anim.start()
        self.fade_out_anim = anim
        
    def minimize_window(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(300)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.finished.connect(self.showMinimized)
        anim.start()
        self.fade_out_anim = anim
    def showEvent(self, event):
        super().showEvent(event)
        if self.windowOpacity() < 1.0:
            self.fade_in()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MyDialog()
    dlg.show()
    sys.exit(app.exec())
