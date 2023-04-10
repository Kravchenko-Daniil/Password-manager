# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QTableView, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 632)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/outline_vpn_key_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_generator = QFrame(self.centralwidget)
        self.frame_generator.setObjectName(u"frame_generator")
        self.frame_generator.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-top-right-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}")
        self.frame_generator.setFrameShape(QFrame.StyledPanel)
        self.frame_generator.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_generator)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_passwordLine = QHBoxLayout()
        self.layout_passwordLine.setObjectName(u"layout_passwordLine")
        self.frame_line = QFrame(self.frame_generator)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 2px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 5px;\n"
"	margin: 0 10px 0 0;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.frame_line.setFrameShape(QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_line)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.password_line = QLineEdit(self.frame_line)
        self.password_line.setObjectName(u"password_line")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setBold(True)
        self.password_line.setFont(font1)
        self.password_line.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"border: none;\n"
"margin: 0;\n"
"font-size: 30px;")

        self.horizontalLayout_5.addWidget(self.password_line)

        self.btn_visibility = QPushButton(self.frame_line)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"margin: 0;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/outline_visibility_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/outline_visibility_off_white_24dp.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon1)
        self.btn_visibility.setIconSize(QSize(26, 26))
        self.btn_visibility.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.btn_visibility)


        self.layout_passwordLine.addWidget(self.frame_line)

        self.btn_refresh = QPushButton(self.frame_generator)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 7px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/outline_refresh_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QSize(45, 45))

        self.layout_passwordLine.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.frame_generator)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 7px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/outline_content_copy_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copy.setIcon(icon3)
        self.btn_copy.setIconSize(QSize(45, 45))
        self.btn_copy.setCheckable(False)
        self.btn_copy.setAutoExclusive(False)

        self.layout_passwordLine.addWidget(self.btn_copy)


        self.verticalLayout_2.addLayout(self.layout_passwordLine)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_lenght = QSlider(self.frame_generator)
        self.slider_lenght.setObjectName(u"slider_lenght")
        self.slider_lenght.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_lenght.setStyleSheet(u"QSlider{\n"
"	margin: 10px 0 10px 0;\n"
"	\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"	background-color: transparent;\n"
"	height: 5px;\n"
"}	\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	background-color:#FF0099;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"	background-color: rgba(255, 255, 255, 180);\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	background-color: white;\n"
"	width: 20px;\n"
"	border-radius: 10px;\n"
"	margin-top: -8px;\n"
"	margin-bottom: -8px;\n"
"}")
        self.slider_lenght.setMinimum(4)
        self.slider_lenght.setMaximum(40)
        self.slider_lenght.setValue(12)
        self.slider_lenght.setOrientation(Qt.Horizontal)

        self.layout_lenght.addWidget(self.slider_lenght)

        self.box_lenght = QSpinBox(self.frame_generator)
        self.box_lenght.setObjectName(u"box_lenght")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.box_lenght.setFont(font2)
        self.box_lenght.setStyleSheet(u"QSpinBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgba(255, 255, 255, 255);\n"
"	padding: 5px;\n"
"	color: white;\n"
"	margin-left: 15px;\n"
"}\n"
"")
        self.box_lenght.setFrame(True)
        self.box_lenght.setAlignment(Qt.AlignCenter)
        self.box_lenght.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.box_lenght.setKeyboardTracking(True)
        self.box_lenght.setProperty("showGroupSeparator", False)
        self.box_lenght.setMinimum(4)
        self.box_lenght.setMaximum(40)
        self.box_lenght.setValue(12)

        self.layout_lenght.addWidget(self.box_lenght)


        self.verticalLayout_2.addLayout(self.layout_lenght)

        self.layout_symbols = QHBoxLayout()
        self.layout_symbols.setObjectName(u"layout_symbols")
        self.btn_lower = QPushButton(self.frame_generator)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setFont(font1)
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgba(255, 255, 255, 150)\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_symbols.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.frame_generator)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setFont(font1)
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgba(255, 255, 255, 150)\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_symbols.addWidget(self.btn_upper)

        self.btn_numbers = QPushButton(self.frame_generator)
        self.btn_numbers.setObjectName(u"btn_numbers")
        self.btn_numbers.setFont(font1)
        self.btn_numbers.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_numbers.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgba(255, 255, 255, 150)\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_numbers.setCheckable(True)
        self.btn_numbers.setChecked(True)

        self.layout_symbols.addWidget(self.btn_numbers)

        self.btn_special = QPushButton(self.frame_generator)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setFont(font1)
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgba(255, 255, 255, 150)\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_special.setCheckable(True)

        self.layout_symbols.addWidget(self.btn_special)


        self.verticalLayout_2.addLayout(self.layout_symbols)


        self.verticalLayout.addWidget(self.frame_generator)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_password = QPushButton(self.btn_frame)
        self.btn_new_password.setObjectName(u"btn_new_password")
        self.btn_new_password.setMinimumSize(QSize(230, 50))
        self.btn_new_password.setFont(font1)
        self.btn_new_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_password.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/outline_post_add_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_password.setIcon(icon4)
        self.btn_new_password.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_new_password)

        self.btn_delete_password = QPushButton(self.btn_frame)
        self.btn_delete_password.setObjectName(u"btn_delete_password")
        self.btn_delete_password.setMinimumSize(QSize(230, 50))
        self.btn_delete_password.setFont(font1)
        self.btn_delete_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_password.setLayoutDirection(Qt.LeftToRight)
        self.btn_delete_password.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    background-color:rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"	height: 35px;\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/outline_delete_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_password.setIcon(icon5)
        self.btn_delete_password.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_password)


        self.verticalLayout.addWidget(self.btn_frame)

        self.frame_table = QFrame(self.centralwidget)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(255, 255, 255, 30); \n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"	color: white;\n"
"}")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_search = QFrame(self.frame_table)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setStyleSheet(u"background-color:rgba(255,255,255,70);\n"
"border: none;\n"
"margin: 0;\n"
"padding: 0;\n"
"border-top-right-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_search = QLineEdit(self.frame_search)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setFont(font1)
        self.line_search.setStyleSheet(u"color: white;\n"
"border: none;\n"
"border-radius: 5px;\n"
"margin: 0;\n"
"background-color:transparent;\n"
"font-size: 18px;\n"
"padding: 5px 0 5px 5px;")

        self.horizontalLayout_2.addWidget(self.line_search)

        self.btn_search = QPushButton(self.frame_search)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255, 255, 255, 20);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/outline_search_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon6)
        self.btn_search.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_search)


        self.verticalLayout_3.addWidget(self.frame_search)

        self.tableView = QTableView(self.frame_table)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font1)
        self.tableView.setFocusPolicy(Qt.NoFocus)
        self.tableView.setLayoutDirection(Qt.LeftToRight)
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: 1px solid rgba(255,255,255,50);\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	alignment: AlignHCenter;\n"
"	alignment: center;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit:focus { \n"
"    background: rgb(53, 53, 53);\n"
"    color: #fff;\n"
"	alignment: AlignHCenter;\n"
"	alignment: center;\n"
"}")
        self.tableView.setLineWidth(10)
        self.tableView.setMidLineWidth(2)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableView.setTextElideMode(Qt.ElideLeft)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(205)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout.addWidget(self.frame_table)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_numbers.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"@&$!#?", None))
        self.btn_new_password.setText(QCoreApplication.translate("MainWindow", u"New password", None))
        self.btn_delete_password.setText(QCoreApplication.translate("MainWindow", u"Delete password", None))
        self.btn_search.setText("")
#if QT_CONFIG(shortcut)
        self.btn_search.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

