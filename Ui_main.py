# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStackedWidget,
    QWidget)

from TempGauge import TemperatureGauge
from fancurve import (FanCurveWidget, FanNoCurveWidget)
import main_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(717, 621)
        self.mainFrame = QFrame(Dialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(40, 40, 641, 541))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet(u"background-color: rgb(251, 251, 251);")
        self.mainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.mainFrame.setLineWidth(0)
        self.topbar = QWidget(self.mainFrame)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setGeometry(QRect(0, 0, 641, 41))
        self.topbar.setAutoFillBackground(False)
        self.close = QPushButton(self.topbar)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(600, 0, 41, 41))
        self.close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/res/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close.setIcon(icon1)
        self.close.setIconSize(QSize(18, 18))
        self.close.setAutoDefault(False)
        self.close.setFlat(True)
        self.minimize = QPushButton(self.topbar)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setGeometry(QRect(559, 0, 40, 40))
        self.minimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimize.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(220, 220, 220);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/res/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize.setIcon(icon2)
        self.minimize.setIconSize(QSize(14, 17))
        self.minimize.setAutoRepeat(False)
        self.minimize.setAutoExclusive(False)
        self.minimize.setAutoDefault(False)
        self.minimize.setFlat(True)
        self.title = QLabel(self.topbar)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(40, 0, 301, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.title.setFont(font)
        self.icon = QLabel(self.topbar)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(10, 9, 25, 25))
        self.icon.setPixmap(QPixmap(u":/icon/res/icon.svg"))
        self.icon.setScaledContents(True)
        self.sidebar = QWidget(self.mainFrame)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 101, 561))
        self.sidebar.setStyleSheet(u"background-color: rgb(249, 246, 238);")
        self.overviewbutton = QPushButton(self.sidebar)
        self.overviewbutton.setObjectName(u"overviewbutton")
        self.overviewbutton.setGeometry(QRect(20, 60, 60, 60))
        self.overviewbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon/res/overview.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.overviewbutton.setIcon(icon3)
        self.overviewbutton.setIconSize(QSize(33, 38))
        self.overviewbutton.setAutoDefault(False)
        self.overviewbutton.setFlat(True)
        self.enclosuresettingbutton = QPushButton(self.sidebar)
        self.enclosuresettingbutton.setObjectName(u"enclosuresettingbutton")
        self.enclosuresettingbutton.setGeometry(QRect(20, 130, 60, 60))
        self.enclosuresettingbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icon/res/disk.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.enclosuresettingbutton.setIcon(icon4)
        self.enclosuresettingbutton.setIconSize(QSize(33, 38))
        self.enclosuresettingbutton.setAutoDefault(False)
        self.enclosuresettingbutton.setFlat(True)
        self.controllersettingbutton = QPushButton(self.sidebar)
        self.controllersettingbutton.setObjectName(u"controllersettingbutton")
        self.controllersettingbutton.setGeometry(QRect(20, 200, 60, 60))
        self.controllersettingbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icon/res/controller.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.controllersettingbutton.setIcon(icon5)
        self.controllersettingbutton.setIconSize(QSize(33, 38))
        self.controllersettingbutton.setAutoDefault(False)
        self.controllersettingbutton.setFlat(True)
        self.oledsettingbutton = QPushButton(self.sidebar)
        self.oledsettingbutton.setObjectName(u"oledsettingbutton")
        self.oledsettingbutton.setGeometry(QRect(20, 270, 60, 60))
        self.oledsettingbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icon/res/display.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.oledsettingbutton.setIcon(icon6)
        self.oledsettingbutton.setIconSize(QSize(33, 38))
        self.oledsettingbutton.setAutoDefault(False)
        self.oledsettingbutton.setFlat(True)
        self.centersettingbutton = QPushButton(self.sidebar)
        self.centersettingbutton.setObjectName(u"centersettingbutton")
        self.centersettingbutton.setGeometry(QRect(20, 340, 60, 60))
        self.centersettingbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icon/res/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.centersettingbutton.setIcon(icon7)
        self.centersettingbutton.setIconSize(QSize(33, 38))
        self.centersettingbutton.setAutoDefault(False)
        self.centersettingbutton.setFlat(True)
        self.aboutbutton = QPushButton(self.sidebar)
        self.aboutbutton.setObjectName(u"aboutbutton")
        self.aboutbutton.setGeometry(QRect(20, 410, 60, 60))
        self.aboutbutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icon/res/about.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aboutbutton.setIcon(icon8)
        self.aboutbutton.setIconSize(QSize(33, 38))
        self.aboutbutton.setAutoDefault(False)
        self.aboutbutton.setFlat(True)
        self.about_interface = QWidget(self.mainFrame)
        self.about_interface.setObjectName(u"about_interface")
        self.about_interface.setGeometry(QRect(99, 40, 541, 501))
        self.label_3 = QLabel(self.about_interface)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 130, 441, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_4 = QLabel(self.about_interface)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 200, 541, 51))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_5 = QLabel(self.about_interface)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 260, 541, 61))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_6 = QLabel(self.about_interface)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 330, 541, 91))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_7 = QLabel(self.about_interface)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 430, 541, 51))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setOpenExternalLinks(True)
        self.label_8 = QLabel(self.about_interface)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 40, 427, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setPixmap(QPixmap(u":/pic/res/TITLE.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)
        self.enclosure_setting_interface = QWidget(self.mainFrame)
        self.enclosure_setting_interface.setObjectName(u"enclosure_setting_interface")
        self.enclosure_setting_interface.setGeometry(QRect(99, 40, 541, 501))
        self.scrollArea = QScrollArea(self.enclosure_setting_interface)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 10, 531, 481))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.scrollArea.setFont(font2)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"QScrollArea QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border-radius: 4px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgba(120, 120, 120, 160);\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:pressed {\n"
"    background: rgba(160, 160, 160, 200);\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical,\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::add-page:vertical,\n"
"QScrollArea QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 531, 481))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 481))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"QScrollArea QWidget {\n"
"    background: transparent;\n"
"}")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 10, 491, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"background-color: transparent;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 70, 231, 401))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        self.groupBox.setFont(font4)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 39, 171, 161))
        self.self_sata1_pwr_checked = QCheckBox(self.groupBox_4)
        self.self_sata1_pwr_checked.setObjectName(u"self_sata1_pwr_checked")
        self.self_sata1_pwr_checked.setGeometry(QRect(30, 80, 121, 19))
        self.self_sata1_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.self_sata1_pwr_checked.setAutoExclusive(False)
        self.self_sata2_pwr_checked = QCheckBox(self.groupBox_4)
        self.self_sata2_pwr_checked.setObjectName(u"self_sata2_pwr_checked")
        self.self_sata2_pwr_checked.setGeometry(QRect(30, 110, 121, 19))
        self.self_sata2_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.self_sata2_pwr_checked.setAutoExclusive(False)
        self.self_nvme_pwr_checked = QCheckBox(self.groupBox_4)
        self.self_nvme_pwr_checked.setObjectName(u"self_nvme_pwr_checked")
        self.self_nvme_pwr_checked.setGeometry(QRect(30, 50, 83, 19))
        self.self_nvme_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.self_nvme_pwr_checked.setAutoExclusive(False)
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 220, 171, 161))
        self.ext_sata1_pwr_checked = QCheckBox(self.groupBox_5)
        self.ext_sata1_pwr_checked.setObjectName(u"ext_sata1_pwr_checked")
        self.ext_sata1_pwr_checked.setGeometry(QRect(30, 80, 121, 19))
        self.ext_sata1_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.ext_sata1_pwr_checked.setAutoExclusive(False)
        self.ext_sata2_pwr_checked = QCheckBox(self.groupBox_5)
        self.ext_sata2_pwr_checked.setObjectName(u"ext_sata2_pwr_checked")
        self.ext_sata2_pwr_checked.setGeometry(QRect(30, 110, 121, 19))
        self.ext_sata2_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.ext_sata2_pwr_checked.setAutoExclusive(False)
        self.ext_nvme_pwr_checked = QCheckBox(self.groupBox_5)
        self.ext_nvme_pwr_checked.setObjectName(u"ext_nvme_pwr_checked")
        self.ext_nvme_pwr_checked.setGeometry(QRect(30, 50, 83, 19))
        self.ext_nvme_pwr_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.ext_nvme_pwr_checked.setAutoExclusive(False)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(270, 70, 231, 171))
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self._1352_pm_checked = QCheckBox(self.groupBox_2)
        self._1352_pm_checked.setObjectName(u"_1352_pm_checked")
        self._1352_pm_checked.setGeometry(QRect(50, 40, 141, 19))
        self._1352_pm_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self._1352_pm_checked.setChecked(True)
        self._1352_pm_checked.setAutoExclusive(True)
        self._1352_jbod_checked = QCheckBox(self.groupBox_2)
        self._1352_jbod_checked.setObjectName(u"_1352_jbod_checked")
        self._1352_jbod_checked.setGeometry(QRect(50, 70, 121, 19))
        self._1352_jbod_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self._1352_jbod_checked.setChecked(False)
        self._1352_jbod_checked.setAutoExclusive(True)
        self._1352_r1_checked = QCheckBox(self.groupBox_2)
        self._1352_r1_checked.setObjectName(u"_1352_r1_checked")
        self._1352_r1_checked.setGeometry(QRect(50, 100, 121, 19))
        self._1352_r1_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self._1352_r1_checked.setAutoExclusive(True)
        self._1352_r0_checked = QCheckBox(self.groupBox_2)
        self._1352_r0_checked.setObjectName(u"_1352_r0_checked")
        self._1352_r0_checked.setGeometry(QRect(50, 130, 121, 19))
        self._1352_r0_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self._1352_r0_checked.setAutoExclusive(True)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(270, 250, 231, 161))
        self.groupBox_3.setFont(font4)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.hddpc_suspend_enable_checked = QCheckBox(self.groupBox_3)
        self.hddpc_suspend_enable_checked.setObjectName(u"hddpc_suspend_enable_checked")
        self.hddpc_suspend_enable_checked.setGeometry(QRect(40, 40, 151, 31))
        self.hddpc_suspend_enable_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.hddpc_suspend_enable_checked.setAutoExclusive(True)
        self.pd_mode_select_combobox = QComboBox(self.groupBox_3)
        self.pd_mode_select_combobox.addItem("")
        self.pd_mode_select_combobox.addItem("")
        self.pd_mode_select_combobox.setObjectName(u"pd_mode_select_combobox")
        self.pd_mode_select_combobox.setGeometry(QRect(40, 110, 151, 31))
        self.pd_mode_select_combobox.setStyleSheet(u"QComboBox {\n"
"    padding: 4px 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    padding: 2px 8px;\n"
"    selection-background-color: #D0D0D0;\n"
"}")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 131, 16))
        self.enclosure_setting_apply = QPushButton(self.scrollAreaWidgetContents_2)
        self.enclosure_setting_apply.setObjectName(u"enclosure_setting_apply")
        self.enclosure_setting_apply.setGeometry(QRect(270, 430, 111, 41))
        self.enclosure_setting_cancel = QPushButton(self.scrollAreaWidgetContents_2)
        self.enclosure_setting_cancel.setObjectName(u"enclosure_setting_cancel")
        self.enclosure_setting_cancel.setGeometry(QRect(390, 430, 111, 41))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.overview_interface = QWidget(self.mainFrame)
        self.overview_interface.setObjectName(u"overview_interface")
        self.overview_interface.setGeometry(QRect(99, 40, 541, 501))
        self.overview_brief = QScrollArea(self.overview_interface)
        self.overview_brief.setObjectName(u"overview_brief")
        self.overview_brief.setGeometry(QRect(-1, 10, 531, 481))
        self.overview_brief.setAutoFillBackground(True)
        self.overview_brief.setStyleSheet(u"QScrollArea QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border-radius: 4px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgba(120, 120, 120, 160);\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:pressed {\n"
"    background: rgba(160, 160, 160, 200);\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical,\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::add-page:vertical,\n"
"QScrollArea QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.overview_brief.setFrameShape(QFrame.Shape.NoFrame)
        self.overview_brief.setFrameShadow(QFrame.Shadow.Plain)
        self.overview_brief.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 531, 481))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 481))
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 491, 51))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: transparent;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.overview_detail = QWidget(self.scrollAreaWidgetContents)
        self.overview_detail.setObjectName(u"overview_detail")
        self.overview_detail.setGeometry(QRect(0, 480, 531, 421))
        self.overview_detail.setStyleSheet(u"background: transparent;")
        self.temp_mp4245 = TemperatureGauge(self.scrollAreaWidgetContents)
        self.temp_mp4245.setObjectName(u"temp_mp4245")
        self.temp_mp4245.setGeometry(QRect(40, 100, 141, 141))
        self.temp_sensor_1 = TemperatureGauge(self.scrollAreaWidgetContents)
        self.temp_sensor_1.setObjectName(u"temp_sensor_1")
        self.temp_sensor_1.setGeometry(QRect(200, 100, 141, 141))
        self.temp_sensor_2 = TemperatureGauge(self.scrollAreaWidgetContents)
        self.temp_sensor_2.setObjectName(u"temp_sensor_2")
        self.temp_sensor_2.setGeometry(QRect(360, 100, 141, 141))
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 80, 131, 16))
        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 240, 141, 20))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(200, 240, 141, 20))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(360, 240, 141, 20))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(40, 280, 461, 191))
        self.groupBox_9.setFont(font4)
        self.groupBox_9.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(130, 20, 91, 131))
        self.groupBox_11.setFont(font4)
        self.groupBox_11.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.sata1_voltage = QLabel(self.groupBox_11)
        self.sata1_voltage.setObjectName(u"sata1_voltage")
        self.sata1_voltage.setGeometry(QRect(3, 30, 85, 31))
        self.sata1_voltage.setStyleSheet(u"background: transparent;")
        self.sata1_voltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata1_current = QLabel(self.groupBox_11)
        self.sata1_current.setObjectName(u"sata1_current")
        self.sata1_current.setGeometry(QRect(3, 60, 85, 31))
        self.sata1_current.setStyleSheet(u"background: transparent;")
        self.sata1_current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata1_consumption = QLabel(self.groupBox_11)
        self.sata1_consumption.setObjectName(u"sata1_consumption")
        self.sata1_consumption.setGeometry(QRect(3, 90, 85, 31))
        self.sata1_consumption.setStyleSheet(u"background: transparent;")
        self.sata1_consumption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(20, 20, 91, 131))
        self.groupBox_12.setFont(font4)
        self.groupBox_12.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.bus_voltage = QLabel(self.groupBox_12)
        self.bus_voltage.setObjectName(u"bus_voltage")
        self.bus_voltage.setGeometry(QRect(3, 48, 85, 31))
        self.bus_voltage.setStyleSheet(u"background: transparent;")
        self.bus_voltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bus_current = QLabel(self.groupBox_12)
        self.bus_current.setObjectName(u"bus_current")
        self.bus_current.setGeometry(QRect(3, 73, 85, 31))
        self.bus_current.setStyleSheet(u"background: transparent;")
        self.bus_current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bus_consumption = QLabel(self.groupBox_12)
        self.bus_consumption.setObjectName(u"bus_consumption")
        self.bus_consumption.setGeometry(QRect(3, 98, 85, 31))
        self.bus_consumption.setStyleSheet(u"background: transparent;")
        self.bus_consumption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mp4245_voltage = QLabel(self.groupBox_12)
        self.mp4245_voltage.setObjectName(u"mp4245_voltage")
        self.mp4245_voltage.setGeometry(QRect(3, 22, 85, 31))
        self.mp4245_voltage.setStyleSheet(u"background: transparent;")
        self.mp4245_voltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_13 = QGroupBox(self.groupBox_9)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(240, 20, 91, 131))
        self.groupBox_13.setFont(font4)
        self.groupBox_13.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.sata2_voltage = QLabel(self.groupBox_13)
        self.sata2_voltage.setObjectName(u"sata2_voltage")
        self.sata2_voltage.setGeometry(QRect(3, 30, 85, 31))
        self.sata2_voltage.setStyleSheet(u"background: transparent;")
        self.sata2_voltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata2_current = QLabel(self.groupBox_13)
        self.sata2_current.setObjectName(u"sata2_current")
        self.sata2_current.setGeometry(QRect(3, 60, 85, 31))
        self.sata2_current.setStyleSheet(u"background: transparent;")
        self.sata2_current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata2_consumption = QLabel(self.groupBox_13)
        self.sata2_consumption.setObjectName(u"sata2_consumption")
        self.sata2_consumption.setGeometry(QRect(3, 90, 85, 31))
        self.sata2_consumption.setStyleSheet(u"background: transparent;")
        self.sata2_consumption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_14 = QGroupBox(self.groupBox_9)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(350, 20, 91, 131))
        self.groupBox_14.setFont(font4)
        self.groupBox_14.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.nvme_voltage = QLabel(self.groupBox_14)
        self.nvme_voltage.setObjectName(u"nvme_voltage")
        self.nvme_voltage.setGeometry(QRect(3, 30, 85, 31))
        self.nvme_voltage.setStyleSheet(u"background: transparent;")
        self.nvme_voltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nvme_current = QLabel(self.groupBox_14)
        self.nvme_current.setObjectName(u"nvme_current")
        self.nvme_current.setGeometry(QRect(3, 60, 85, 31))
        self.nvme_current.setStyleSheet(u"background: transparent;")
        self.nvme_current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nvme_consumption = QLabel(self.groupBox_14)
        self.nvme_consumption.setObjectName(u"nvme_consumption")
        self.nvme_consumption.setGeometry(QRect(3, 90, 85, 31))
        self.nvme_consumption.setStyleSheet(u"background: transparent;")
        self.nvme_consumption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata2_pwr_stat_checked = QCheckBox(self.groupBox_9)
        self.sata2_pwr_stat_checked.setObjectName(u"sata2_pwr_stat_checked")
        self.sata2_pwr_stat_checked.setGeometry(QRect(280, 160, 81, 21))
        self.sata2_pwr_stat_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.sata2_pwr_stat_checked.setCheckable(False)
        self.nvme_pwr_stat_checked = QCheckBox(self.groupBox_9)
        self.nvme_pwr_stat_checked.setObjectName(u"nvme_pwr_stat_checked")
        self.nvme_pwr_stat_checked.setGeometry(QRect(367, 160, 83, 21))
        self.nvme_pwr_stat_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.nvme_pwr_stat_checked.setCheckable(False)
        self.sata1_pwr_stat_checked = QCheckBox(self.groupBox_9)
        self.sata1_pwr_stat_checked.setObjectName(u"sata1_pwr_stat_checked")
        self.sata1_pwr_stat_checked.setGeometry(QRect(180, 160, 91, 21))
        self.sata1_pwr_stat_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.sata1_pwr_stat_checked.setCheckable(False)
        self.label_23 = QLabel(self.groupBox_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(25, 160, 151, 21))
        self.self_pwr_stat_checked = QCheckBox(self.scrollAreaWidgetContents)
        self.self_pwr_stat_checked.setObjectName(u"self_pwr_stat_checked")
        self.self_pwr_stat_checked.setGeometry(QRect(390, 30, 111, 19))
        self.self_pwr_stat_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.self_pwr_stat_checked.setCheckable(False)
        self.ext_pwr_stat_checked = QCheckBox(self.scrollAreaWidgetContents)
        self.ext_pwr_stat_checked.setObjectName(u"ext_pwr_stat_checked")
        self.ext_pwr_stat_checked.setGeometry(QRect(390, 60, 111, 19))
        self.ext_pwr_stat_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.ext_pwr_stat_checked.setCheckable(False)
        self.overview_brief.setWidget(self.scrollAreaWidgetContents)
        self.controller_setting_interface = QWidget(self.mainFrame)
        self.controller_setting_interface.setObjectName(u"controller_setting_interface")
        self.controller_setting_interface.setGeometry(QRect(99, 40, 541, 501))
        self.scrollArea1 = QScrollArea(self.controller_setting_interface)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setGeometry(QRect(-1, 10, 531, 481))
        self.scrollArea1.setAutoFillBackground(True)
        self.scrollArea1.setStyleSheet(u"QScrollArea QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border-radius: 4px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgba(120, 120, 120, 160);\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:pressed {\n"
"    background: rgba(160, 160, 160, 200);\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical,\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::add-page:vertical,\n"
"QScrollArea QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea1.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea1.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollAreaWidgetContents1 = QWidget()
        self.scrollAreaWidgetContents1.setObjectName(u"scrollAreaWidgetContents1")
        self.scrollAreaWidgetContents1.setGeometry(QRect(0, 0, 531, 481))
        self.scrollAreaWidgetContents1.setMinimumSize(QSize(0, 481))
        self.label_11 = QLabel(self.scrollAreaWidgetContents1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 10, 491, 51))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background-color: transparent;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(40, 290, 171, 181))
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.reset_only_btn = QPushButton(self.groupBox_6)
        self.reset_only_btn.setObjectName(u"reset_only_btn")
        self.reset_only_btn.setGeometry(QRect(30, 30, 111, 41))
        self.reset_to_dfu_btn = QPushButton(self.groupBox_6)
        self.reset_to_dfu_btn.setObjectName(u"reset_to_dfu_btn")
        self.reset_to_dfu_btn.setGeometry(QRect(30, 80, 111, 41))
        self.dfu_update_btn = QPushButton(self.groupBox_6)
        self.dfu_update_btn.setObjectName(u"dfu_update_btn")
        self.dfu_update_btn.setGeometry(QRect(30, 130, 111, 41))
        self.controller_setting_cancel = QPushButton(self.scrollAreaWidgetContents1)
        self.controller_setting_cancel.setObjectName(u"controller_setting_cancel")
        self.controller_setting_cancel.setGeometry(QRect(390, 430, 111, 41))
        self.controller_setting_apply = QPushButton(self.scrollAreaWidgetContents1)
        self.controller_setting_apply.setObjectName(u"controller_setting_apply")
        self.controller_setting_apply.setGeometry(QRect(270, 430, 111, 41))
        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents1)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(40, 60, 461, 221))
        self.groupBox_7.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 30, 2, 180))
        self.label.setStyleSheet(u"background-color: rgb(161, 161, 161);")
        self.curve_mode_btn = QCheckBox(self.groupBox_7)
        self.curve_mode_btn.setObjectName(u"curve_mode_btn")
        self.curve_mode_btn.setGeometry(QRect(330, 90, 111, 19))
        self.curve_mode_btn.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.curve_mode_btn.setCheckable(True)
        self.curve_mode_btn.setChecked(True)
        self.curve_mode_btn.setAutoExclusive(True)
        self.fixed_mode_btn = QCheckBox(self.groupBox_7)
        self.fixed_mode_btn.setObjectName(u"fixed_mode_btn")
        self.fixed_mode_btn.setGeometry(QRect(330, 130, 111, 19))
        self.fixed_mode_btn.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.fixed_mode_btn.setCheckable(True)
        self.fixed_mode_btn.setAutoExclusive(True)
        self.fullon_mode_btn = QCheckBox(self.groupBox_7)
        self.fullon_mode_btn.setObjectName(u"fullon_mode_btn")
        self.fullon_mode_btn.setGeometry(QRect(330, 170, 111, 19))
        self.fullon_mode_btn.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.fullon_mode_btn.setCheckable(True)
        self.fullon_mode_btn.setAutoExclusive(True)
        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 50, 111, 21))
        self.FanSettingWidget = QStackedWidget(self.groupBox_7)
        self.FanSettingWidget.setObjectName(u"FanSettingWidget")
        self.FanSettingWidget.setGeometry(QRect(19, 30, 271, 181))
        self.FanCurveSetting = FanCurveWidget()
        self.FanCurveSetting.setObjectName(u"FanCurveSetting")
        self.FanSettingWidget.addWidget(self.FanCurveSetting)
        self.FanNoCurveWidget = FanNoCurveWidget()
        self.FanNoCurveWidget.setObjectName(u"FanNoCurveWidget")
        self.FanSettingWidget.addWidget(self.FanNoCurveWidget)
        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents1)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(230, 290, 271, 121))
        self.groupBox_8.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    margin-top: 16px;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #444444;\n"
"    font-size: 12px;\n"
"}")
        self.label_18 = QLabel(self.groupBox_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 40, 161, 21))
        self.temp_setting_spinbox = QSpinBox(self.groupBox_8)
        self.temp_setting_spinbox.setObjectName(u"temp_setting_spinbox")
        self.temp_setting_spinbox.setGeometry(QRect(90, 70, 70, 31))
        self.temp_setting_spinbox.setMaximum(100)
        self.temp_setting_spinbox.setValue(40)
        self.temp_setting_show = QLabel(self.groupBox_8)
        self.temp_setting_show.setObjectName(u"temp_setting_show")
        self.temp_setting_show.setGeometry(QRect(170, 70, 41, 31))
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents1)
        self.oled_setting_interface = QWidget(self.mainFrame)
        self.oled_setting_interface.setObjectName(u"oled_setting_interface")
        self.oled_setting_interface.setGeometry(QRect(99, 40, 541, 501))
        self.scrollArea2 = QScrollArea(self.oled_setting_interface)
        self.scrollArea2.setObjectName(u"scrollArea2")
        self.scrollArea2.setGeometry(QRect(-1, 10, 531, 481))
        self.scrollArea2.setAutoFillBackground(True)
        self.scrollArea2.setStyleSheet(u"QScrollArea QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border-radius: 4px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgba(120, 120, 120, 160);\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:pressed {\n"
"    background: rgba(160, 160, 160, 200);\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical,\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::add-page:vertical,\n"
"QScrollArea QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea2.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName(u"scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 523, 900))
        self.scrollAreaWidgetContents2.setMinimumSize(QSize(0, 900))
        self.label_13 = QLabel(self.scrollAreaWidgetContents2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 10, 491, 51))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"background-color: transparent;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_15 = QLabel(self.scrollAreaWidgetContents2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 220, 501, 41))
        self.label_15.setStyleSheet(u"background-color: transparent;")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)
        self.center_setting_interface = QWidget(self.mainFrame)
        self.center_setting_interface.setObjectName(u"center_setting_interface")
        self.center_setting_interface.setGeometry(QRect(99, 40, 541, 501))
        self.scrollArea3 = QScrollArea(self.center_setting_interface)
        self.scrollArea3.setObjectName(u"scrollArea3")
        self.scrollArea3.setGeometry(QRect(-1, 10, 531, 481))
        self.scrollArea3.setAutoFillBackground(False)
        self.scrollArea3.setStyleSheet(u"QScrollArea QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border-radius: 4px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgba(120, 120, 120, 160);\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical:pressed {\n"
"    background: rgba(160, 160, 160, 200);\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical,\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::add-page:vertical,\n"
"QScrollArea QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea3.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea3.setWidgetResizable(True)
        self.scrollAreaWidgetContents3 = QWidget()
        self.scrollAreaWidgetContents3.setObjectName(u"scrollAreaWidgetContents3")
        self.scrollAreaWidgetContents3.setGeometry(QRect(0, 0, 531, 481))
        self.scrollAreaWidgetContents3.setMinimumSize(QSize(0, 481))
        self.label_10 = QLabel(self.scrollAreaWidgetContents3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 10, 491, 51))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background-color: transparent;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.firmware_update_checked = QCheckBox(self.scrollAreaWidgetContents3)
        self.firmware_update_checked.setObjectName(u"firmware_update_checked")
        self.firmware_update_checked.setGeometry(QRect(60, 100, 381, 21))
        self.firmware_update_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.center_update_checked = QCheckBox(self.scrollAreaWidgetContents3)
        self.center_update_checked.setObjectName(u"center_update_checked")
        self.center_update_checked.setGeometry(QRect(60, 140, 381, 21))
        self.center_update_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.launch_system_startup_checked = QCheckBox(self.scrollAreaWidgetContents3)
        self.launch_system_startup_checked.setObjectName(u"launch_system_startup_checked")
        self.launch_system_startup_checked.setGeometry(QRect(60, 180, 381, 21))
        self.launch_system_startup_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.minimized_startup_checked = QCheckBox(self.scrollAreaWidgetContents3)
        self.minimized_startup_checked.setObjectName(u"minimized_startup_checked")
        self.minimized_startup_checked.setGeometry(QRect(60, 220, 381, 21))
        self.minimized_startup_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.center_setting_cancel = QPushButton(self.scrollAreaWidgetContents3)
        self.center_setting_cancel.setObjectName(u"center_setting_cancel")
        self.center_setting_cancel.setGeometry(QRect(390, 430, 111, 41))
        self.center_setting_apply = QPushButton(self.scrollAreaWidgetContents3)
        self.center_setting_apply.setObjectName(u"center_setting_apply")
        self.center_setting_apply.setGeometry(QRect(270, 430, 111, 41))
        self.fahrenheit_celsius_switch_checked = QCheckBox(self.scrollAreaWidgetContents3)
        self.fahrenheit_celsius_switch_checked.setObjectName(u"fahrenheit_celsius_switch_checked")
        self.fahrenheit_celsius_switch_checked.setGeometry(QRect(60, 260, 381, 21))
        self.fahrenheit_celsius_switch_checked.setStyleSheet(u"QCheckBox {\n"
"    background: transparent;\n"
"}")
        self.scrollArea3.setWidget(self.scrollAreaWidgetContents3)
        self.sidebar.raise_()
        self.topbar.raise_()
        self.about_interface.raise_()
        self.oled_setting_interface.raise_()
        self.center_setting_interface.raise_()
        self.enclosure_setting_interface.raise_()
        self.overview_interface.raise_()
        self.controller_setting_interface.raise_()

        self.retranslateUi(Dialog)

        self.pd_mode_select_combobox.setCurrentIndex(0)
        self.FanSettingWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.close.setText("")
        self.minimize.setText("")
        self.title.setText(QCoreApplication.translate("Dialog", u"R-SODIUM Ultra 2 Control Center", None))
        self.icon.setText("")
#if QT_CONFIG(tooltip)
        self.overviewbutton.setToolTip(QCoreApplication.translate("Dialog", u"Overview", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.overviewbutton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.overviewbutton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.overviewbutton.setText("")
#if QT_CONFIG(tooltip)
        self.enclosuresettingbutton.setToolTip(QCoreApplication.translate("Dialog", u"Enclosure Setting", None))
#endif // QT_CONFIG(tooltip)
        self.enclosuresettingbutton.setText("")
#if QT_CONFIG(tooltip)
        self.controllersettingbutton.setToolTip(QCoreApplication.translate("Dialog", u"Controller Setting", None))
#endif // QT_CONFIG(tooltip)
        self.controllersettingbutton.setText("")
#if QT_CONFIG(tooltip)
        self.oledsettingbutton.setToolTip(QCoreApplication.translate("Dialog", u"OLED Display Setting", None))
#endif // QT_CONFIG(tooltip)
        self.oledsettingbutton.setText("")
#if QT_CONFIG(tooltip)
        self.centersettingbutton.setToolTip(QCoreApplication.translate("Dialog", u"Center Setting", None))
#endif // QT_CONFIG(tooltip)
        self.centersettingbutton.setText("")
#if QT_CONFIG(tooltip)
        self.aboutbutton.setToolTip(QCoreApplication.translate("Dialog", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.aboutbutton.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>This software is opensourced on GitHub:</p><p><a href=\"https://github.com/barryblueice/R-SODIUM-Ultra-2-Control-Center\"><span style=\" text-decoration: underline; color:#003e92;\">barryblueice - R-SODIUM-Ultra-2-Control-Center</span></a></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Additionally, related firmware is also opensourced on GitHub:</p><p><a href=\"https://github.com/barryblueice/R-SODIUM-Ultra-2-Enclosure-Docker-Station-Firmware\"><span style=\" text-decoration: underline; color:#003e92;\">barryblueice - R-SODIUM-Ultra-2-Station-Firmware</span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\n"
"<html><head/><body><p>Hardware is opensourced on OSHWHUB:</p><p><a href=\"https://oshwhub.com/barryblueice/usb3-ultra-2-docker-station\"><span style=\" text-decoration: underline; color:#003e92;\">https://oshwhub.com/barryblueice/usb3-ultra-2-docker-station</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>This software is opensource under <a href=\"https://www.mozilla.org/en-US/MPL/2.0/\"><span style=\" text-decoration: underline; color:#003e92;\">Mozilla Public License Version 2.0</span></a><a href=\"https://www.mozilla.org/en-US/MPL/2.0/\"><span style=\" color:#003e92;\">.</span></a></p><p>Additionally, hardware is opensource under</p><p><a href=\"https://gitlab.com/ohwr/project/cernohl/-/wikis/uploads/819d71bea3458f71fba6cf4fb0f2de6b/cern_ohl_s_v2.txt\"><span style=\" text-decoration: underline; color:#003e92;\">CERN License - Strongly Reciprocal</span></a><a href=\"https://gitlab.com/ohwr/project/cernohl/-/wikis/uploads/819d71bea3458f71fba6cf4fb0f2de6b/cern_ohl_s_v2.txt\"><span style=\" color:#003e92;\">.</span></a><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Hope you enjoy my work! :)</p></body></html>", None))
        self.label_8.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Enclosure Setting", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"DISK On-Power Config:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Self-Powered:", None))
        self.self_sata1_pwr_checked.setText(QCoreApplication.translate("Dialog", u"SATA1 (NGFF)", None))
        self.self_sata2_pwr_checked.setText(QCoreApplication.translate("Dialog", u"SATA2 (2.5)", None))
        self.self_nvme_pwr_checked.setText(QCoreApplication.translate("Dialog", u"NVMe", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Ext-Powered:", None))
        self.ext_sata1_pwr_checked.setText(QCoreApplication.translate("Dialog", u"SATA1 (NGFF)", None))
        self.ext_sata2_pwr_checked.setText(QCoreApplication.translate("Dialog", u"SATA2 (2.5)", None))
        self.ext_nvme_pwr_checked.setText(QCoreApplication.translate("Dialog", u"NVMe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"ASM1352R Config:", None))
        self._1352_pm_checked.setText(QCoreApplication.translate("Dialog", u"SATA-PM (Default)", None))
        self._1352_jbod_checked.setText(QCoreApplication.translate("Dialog", u"JBOD (Span)", None))
        self._1352_r1_checked.setText(QCoreApplication.translate("Dialog", u"RAID 1", None))
        self._1352_r0_checked.setText(QCoreApplication.translate("Dialog", u"RAID 0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Other Config:", None))
        self.hddpc_suspend_enable_checked.setText(QCoreApplication.translate("Dialog", u"Enable suspend by\n"
"HDDPC signal", None))
        self.pd_mode_select_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"Force PD Mode", None))
        self.pd_mode_select_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"Adaptive PD Mode", None))

#if QT_CONFIG(tooltip)
        self.pd_mode_select_combobox.setToolTip(QCoreApplication.translate("Dialog", u"Choose PD Mode for PD charging port", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PD Mode Control:", None))
        self.enclosure_setting_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.enclosure_setting_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Temperature Status:", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"MP4245 Temp.", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Sensor #1 Temp.", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Sensor #2 Temp.", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"Power Status Monitor:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Dialog", u"SATA NGFF:", None))
        self.sata1_voltage.setText(QCoreApplication.translate("Dialog", u"U: 0.00 V", None))
        self.sata1_current.setText(QCoreApplication.translate("Dialog", u"I: 0.00 A", None))
        self.sata1_consumption.setText(QCoreApplication.translate("Dialog", u"P: 0.00 W", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Dialog", u"BUS:", None))
        self.bus_voltage.setText(QCoreApplication.translate("Dialog", u"U2: 0.00 V", None))
        self.bus_current.setText(QCoreApplication.translate("Dialog", u"I: 0.00 A", None))
        self.bus_consumption.setText(QCoreApplication.translate("Dialog", u"P: 0.00 W", None))
        self.mp4245_voltage.setText(QCoreApplication.translate("Dialog", u"U1: 0.00 V", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Dialog", u"SATA 2.5:", None))
        self.sata2_voltage.setText(QCoreApplication.translate("Dialog", u"U: 0.00 V", None))
        self.sata2_current.setText(QCoreApplication.translate("Dialog", u"I: 0.00 A", None))
        self.sata2_consumption.setText(QCoreApplication.translate("Dialog", u"P: 0.00 W", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Dialog", u"NVMe:", None))
        self.nvme_voltage.setText(QCoreApplication.translate("Dialog", u"U: 0.00 V", None))
        self.nvme_current.setText(QCoreApplication.translate("Dialog", u"I: 0.00 A", None))
        self.nvme_consumption.setText(QCoreApplication.translate("Dialog", u"P: 0.00 W", None))
        self.sata2_pwr_stat_checked.setText(QCoreApplication.translate("Dialog", u"SATA 2.5", None))
        self.nvme_pwr_stat_checked.setText(QCoreApplication.translate("Dialog", u"NVMe", None))
        self.sata1_pwr_stat_checked.setText(QCoreApplication.translate("Dialog", u"SATA NGFF", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Disk(s) On-Power Status:", None))
        self.self_pwr_stat_checked.setText(QCoreApplication.translate("Dialog", u"Self-Powered", None))
        self.ext_pwr_stat_checked.setText(QCoreApplication.translate("Dialog", u"Ext-Powered", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Controller Setting", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Advanced Option:", None))
        self.reset_only_btn.setText(QCoreApplication.translate("Dialog", u"Reset Only", None))
        self.reset_to_dfu_btn.setText(QCoreApplication.translate("Dialog", u"Reset to DFU", None))
        self.dfu_update_btn.setText(QCoreApplication.translate("Dialog", u"DFU Updater", None))
        self.controller_setting_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.controller_setting_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Fan Setting:", None))
        self.label.setText("")
        self.curve_mode_btn.setText(QCoreApplication.translate("Dialog", u"Curve Mode", None))
        self.fixed_mode_btn.setText(QCoreApplication.translate("Dialog", u"Fixed Mode", None))
        self.fullon_mode_btn.setText(QCoreApplication.translate("Dialog", u"Full-on Mode", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Fan Mode Select:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"RGB LED Setting:", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Temp. Warning Threshold:", None))
        self.temp_setting_show.setText(QCoreApplication.translate("Dialog", u"\u00b0C", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"OLED Display Setting", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Under development. \n"
"Stay tuned for updates.", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Center Setting", None))
        self.firmware_update_checked.setText(QCoreApplication.translate("Dialog", u"Automatically check firmware update when device attached", None))
        self.center_update_checked.setText(QCoreApplication.translate("Dialog", u"Automatically check for updates on startup", None))
        self.launch_system_startup_checked.setText(QCoreApplication.translate("Dialog", u"Launch center automatically after system startup", None))
        self.minimized_startup_checked.setText(QCoreApplication.translate("Dialog", u"Minimized the center after center startup", None))
        self.center_setting_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.center_setting_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.fahrenheit_celsius_switch_checked.setText(QCoreApplication.translate("Dialog", u"Use Fahrenheit for temperature (Celsius by default)", None))
    # retranslateUi

