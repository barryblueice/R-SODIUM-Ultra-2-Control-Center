import sys
from PySide6.QtWidgets import QApplication, QDialog, QWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from Ui_main import Ui_Dialog

import interface_controller

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.overview_interface.setVisible(True)
        self.ui.enclosure_setting_interface.setVisible(False)
        self.ui.controller_setting_interface.setVisible(False)
        self.ui.oled_setting_interface.setVisible(False)
        self.ui.center_setting_interface.setVisible(False)
        self.ui.about_interface.setVisible(False)
        
        self.ui.overviewbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.overview_interface)
        )
        self.ui.enclosuresettingbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.enclosure_setting_interface)
        )
        self.ui.controllersettingbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.controller_setting_interface)
        )
        self.ui.oledsettingbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.oled_setting_interface)
        )
        self.ui.centersettingbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.center_setting_interface)
        )
        self.ui.aboutbutton.clicked.connect(
            lambda: self.interface_visable_controller.activate_only(self.ui.about_interface)
        )

        self.qwidget_list = [
            self.ui.overview_interface,
            self.ui.enclosure_setting_interface,
            self.ui.controller_setting_interface,
            self.ui.oled_setting_interface,
            self.ui.center_setting_interface,
            self.ui.about_interface
            ]
        
        self.interface_visable_controller = interface_controller.GroupVisibilityController()
        self.interface_visable_controller.switch_signal.connect(self.show_only_one)
        self.interface_visable_controller.set_all_widgets(self.qwidget_list)


        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setWindowOpacity(0.0)
        self.show()
        self.fade_in()

        self.ui.close.clicked.connect(self.fade_out_close)
        self.ui.minimize.clicked.connect(self.minimize_window)
        
    def ui_state(self,status: bool):
        self.ui_status = status
            
    def fade_in(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(150)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()
        self.fade_in_anim = anim
        
    def fade_out_close(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(150)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.finished.connect(QApplication.quit)
        anim.start()
        self.fade_out_anim = anim
        
    def minimize_window(self):
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(150)
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
            
    def show_only_one(self, target_widget):
        qw: QWidget
        for qw in self.qwidget_list:
            qw.setVisible(qw == target_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MainDialog()
    dlg.show()
    sys.exit(app.exec())
