import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtCore import Qt
from Ui_main import Ui_Dialog
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSystemTrayIcon
from PySide6.QtGui import QColor

shadow = QGraphicsDropShadowEffect()

shadow.setBlurRadius(20)
shadow.setColor(QColor(0, 0, 0, 70))
shadow.setOffset(0, 2)

import ui.func.interface_controller as interface_controller
import ui.func.checked_controller as checked_controller

from ui.animation.widget_ani import WidgetAni
from ui.animation.widget_drag import WidgetDrag

from ui.widgets.toast import NotificationBar
from ui.widgets.trayicon import TrayIconWidget

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.drag_helper = WidgetDrag(self, self.ui.topbar)
        
        self.ui.mainFrame.setGraphicsEffect(shadow)
        
        self.ui.overview_interface.setVisible(True)
        self.ui.enclosure_setting_interface.setVisible(False)
        self.ui.controller_setting_interface.setVisible(False)
        self.ui.oled_setting_interface.setVisible(False)
        self.ui.center_setting_interface.setVisible(False)
        self.ui.about_interface.setVisible(False)
        
        self.ui.FanSettingDisabledWidget.setVisible(False)
        
        self.ui.ext_pwr_stat_checked.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.ui.self_pwr_stat_checked.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.ui.sata1_pwr_stat_checked.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.ui.sata2_pwr_stat_checked.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.ui.nvme_pwr_stat_checked.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        
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
        self.interface_visable_controller.switch_signal.connect(self.show_only_one_widgeted)
        self.interface_visable_controller.set_all_widgets(self.qwidget_list)
        
        self.fan_checked_list = [
            self.ui.curve_mode_checked,
            self.ui.fixed_mode_checked,
            self.ui.fullon_mode_checked
        ]
        
        self.fan_curve_visable_controller = checked_controller.FanCurveVisabilityController()
        self.fan_curve_visable_controller.switch_signal.connect(self.fancurve_visable_control)
        self.fan_curve_visable_controller.set_all_widgets(self.fan_checked_list)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setWindowOpacity(0.0)
        self.show()
        WidgetAni.fade_in(self)
        
        self._drag_active = False
        self._drag_position = None

        self.ui.close.clicked.connect(lambda: WidgetAni.fade_out_close(self))
        # self.ui.close.clicked.connect(lambda:WidgetAni.minimize_window(self))
        self.ui.close.clicked.connect(self.closeEvent)
        self.ui.minimize.clicked.connect(lambda:WidgetAni.minimize_window(self))
        
        self.trayicon = TrayIconWidget(self)

    def closeEvent(self, event):
        NotificationBar.show_notification("The center has minimized to tray.")
        pass
        
    def ui_state(self,status: bool):
        self.ui_status = status
            
    def show_only_one_widgeted(self, target_widget):
        qw: QWidget
        for qw in self.qwidget_list:
            qw.setVisible(qw == target_widget)
            
    def fancurve_visable_control(self, index):
        match index:
            case 2:
                self.ui.FanSettingDisabledWidget.setVisible(True)
                self.ui.FanSettingWidget.setEnabled(False)
            case _:
                self.ui.FanSettingDisabledWidget.setVisible(False)
                self.ui.FanSettingWidget.setEnabled(True)
                self.ui.FanSettingWidget.setCurrentIndex(index)
                # self.ui.FanSettingWidget.setCurrentIndex(index)
                
            
    def mousePressEvent(self, event):
        self.drag_helper.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.drag_helper.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_helper.mouseReleaseEvent(event)