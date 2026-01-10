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
    QScrollArea, QSizePolicy, QWidget)
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
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 531, 481))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 481))
        self.scrollAreaWidgetContents.setStyleSheet(u"QScrollArea QWidget {\n"
"    background: transparent;\n"
"}")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 10, 491, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"background-color: transparent;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
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
        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 80, 121, 19))
        self.checkBox_2.setAutoExclusive(False)
        self.checkBox_3 = QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(30, 110, 121, 19))
        self.checkBox_3.setAutoExclusive(False)
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 50, 83, 19))
        self.checkBox.setAutoExclusive(False)
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 220, 171, 161))
        self.checkBox_9 = QCheckBox(self.groupBox_5)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(30, 80, 121, 19))
        self.checkBox_9.setAutoExclusive(False)
        self.checkBox_10 = QCheckBox(self.groupBox_5)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(30, 110, 121, 19))
        self.checkBox_10.setAutoExclusive(False)
        self.checkBox_11 = QCheckBox(self.groupBox_5)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(30, 50, 83, 19))
        self.checkBox_11.setAutoExclusive(False)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
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
        self.checkBox_6 = QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(50, 40, 141, 19))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setAutoExclusive(True)
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(50, 70, 121, 19))
        self.checkBox_4.setAutoExclusive(True)
        self.checkBox_5 = QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(50, 100, 121, 19))
        self.checkBox_5.setAutoExclusive(True)
        self.checkBox_7 = QCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(50, 130, 121, 19))
        self.checkBox_7.setAutoExclusive(True)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
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
        self.checkBox_8 = QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(40, 40, 151, 31))
        self.checkBox_8.setAutoExclusive(True)
        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 110, 151, 31))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
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
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 430, 111, 41))
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 430, 111, 41))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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
        self.scrollAreaWidgetContents1 = QWidget()
        self.scrollAreaWidgetContents1.setObjectName(u"scrollAreaWidgetContents1")
        self.scrollAreaWidgetContents1.setGeometry(QRect(0, 0, 523, 900))
        self.scrollAreaWidgetContents1.setMinimumSize(QSize(0, 900))
        self.label_9 = QLabel(self.scrollAreaWidgetContents1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 491, 51))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: transparent;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.overview_detail = QWidget(self.scrollAreaWidgetContents1)
        self.overview_detail.setObjectName(u"overview_detail")
        self.overview_detail.setGeometry(QRect(0, 420, 531, 481))
        self.overview_detail.setStyleSheet(u"background: transparent;")
        self.overview_brief.setWidget(self.scrollAreaWidgetContents1)
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
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName(u"scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 523, 900))
        self.scrollAreaWidgetContents2.setMinimumSize(QSize(0, 900))
        self.label_11 = QLabel(self.scrollAreaWidgetContents2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 10, 491, 51))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background-color: transparent;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents2)
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
        self.scrollAreaWidgetContents3 = QWidget()
        self.scrollAreaWidgetContents3.setObjectName(u"scrollAreaWidgetContents3")
        self.scrollAreaWidgetContents3.setGeometry(QRect(0, 0, 523, 900))
        self.scrollAreaWidgetContents3.setMinimumSize(QSize(0, 900))
        self.label_13 = QLabel(self.scrollAreaWidgetContents3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 10, 491, 51))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"background-color: transparent;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents3)
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
        self.scrollAreaWidgetContents4 = QWidget()
        self.scrollAreaWidgetContents4.setObjectName(u"scrollAreaWidgetContents4")
        self.scrollAreaWidgetContents4.setGeometry(QRect(0, 0, 523, 900))
        self.scrollAreaWidgetContents4.setMinimumSize(QSize(0, 900))
        self.label_10 = QLabel(self.scrollAreaWidgetContents4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 10, 491, 51))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background-color: transparent;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollArea3.setWidget(self.scrollAreaWidgetContents4)
        self.sidebar.raise_()
        self.topbar.raise_()
        self.center_setting_interface.raise_()
        self.controller_setting_interface.raise_()
        self.oled_setting_interface.raise_()
        self.overview_interface.raise_()
        self.enclosure_setting_interface.raise_()
        self.about_interface.raise_()

        self.retranslateUi(Dialog)

        self.comboBox.setCurrentIndex(0)


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
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"SATA1 (NGFF)", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"SATA2 (2.5)", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"NVMe", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Ext-Powered:", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"SATA1 (NGFF)", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"SATA2 (2.5)", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"NVMe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"ASM1352R Config:", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"SATA-PM (Default)", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"JBOD (Span)", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"RAID 1", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"RAID 0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Other Config:", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Enable suspend by\n"
"HDDPC signal", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Force PD Mode", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Adaptive PD Mode", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Dialog", u"Choose PD Mode for PD charging port", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PD Mode Control:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Controller Setting", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"OLED Display Setting", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Center Setting", None))
    # retranslateUi

