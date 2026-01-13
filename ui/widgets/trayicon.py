import os
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QDialog

class TrayIconWidget:
    def __init__(self, main_window: QDialog):
        self.main_window = main_window
        
        icon_path = os.path.join(os.getcwd(), "res", "icon", "icon.svg")
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self.main_window)
        self.tray_icon.setToolTip("R-SODIUM Ultra 2 Control Center")

        self.menu = QMenu()
        
        self.show_action = QAction("Show", self.main_window)
        self.quit_action = QAction("Exit", self.main_window)

        self.show_action.triggered.connect(self.main_window.showNormal)
        self.show_action.triggered.connect(self.main_window.activateWindow)
        
        self.quit_action.triggered.connect(self.TrayIconQuitEvent)

        self.menu.addAction(self.show_action)
        self.menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()
        
    def TrayIconQuitEvent(self, event):
        QtWidgets.QApplication.quit()