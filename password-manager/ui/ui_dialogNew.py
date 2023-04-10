# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialogNew.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(328, 353)
        Dialog.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-top-right-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 161, 41))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 22px;\n"
"background-color: transparent;\n"
"border: none;")
        self.line_service = QLineEdit(self.frame)
        self.line_service.setObjectName(u"line_service")
        self.line_service.setGeometry(QRect(70, 90, 161, 31))
        self.line_service.setStyleSheet(u"QLineEdit{\n"
"	font-size: 16px;\n"
"	color: white;\n"
"	padding-left:7px;\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        self.line_login = QLineEdit(self.frame)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(70, 140, 161, 31))
        self.line_login.setStyleSheet(u"QLineEdit{\n"
"	font-size: 16px;\n"
"	color: white;\n"
"	padding-left: 5px;\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")
        self.line_password = QLineEdit(self.frame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(70, 190, 161, 31))
        self.line_password.setStyleSheet(u"QLineEdit{\n"
"	font-size: 16px;\n"
"	color: white;\n"
"	padding-left: 5px;\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 5px;\n"
"	\n"
"}")
        self.line_password.setInputMask(u"")
        self.line_password.setMaxLength(40)
        self.line_password.setFrame(True)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setClearButtonEnabled(False)
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(70, 250, 161, 51))
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgba(255, 255, 255, 150)\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"New password", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"New password", None))
        self.line_service.setPlaceholderText(QCoreApplication.translate("Dialog", u"Service", None))
        self.line_login.setPlaceholderText(QCoreApplication.translate("Dialog", u"Login", None))
        self.line_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"Save new password", None))
    # retranslateUi

