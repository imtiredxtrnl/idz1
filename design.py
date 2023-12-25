# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QTextBrowser, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"background-color:#282828;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1281, 721))
        self.tabWidget.setStyleSheet(u"QTabWidget{\n"
"border: none;\n"
"}         \n"
"  QTabBar::tab {\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border-radius:15px;\n"
"padding:10px 5px;\n"
"margin: 5px 3px;\n"
"background-color: #280886;\n"
"color:#FFFFFF;\n"
"            }\n"
"           QTabBar::tab:selected {\n"
"                background-color: #5215fc;\n"
"            }")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setDocumentMode(False)
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        self.tabMain.setStyleSheet(u"border:none;")
        self.textBrowser = QTextBrowser(self.tabMain)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 1211, 421))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"  background-color: #ffffff;\n"
"  color: #000000;\n"
"  font-family: Arial;\n"
"  font-size: 12pt;\n"
" border-radius:15px;\n"
"}")
        self.gridLayoutWidget = QWidget(self.tabMain)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(150, 480, 957, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.btnOpenFile = QPushButton(self.gridLayoutWidget)
        self.btnOpenFile.setObjectName(u"btnOpenFile")
        self.btnOpenFile.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"    padding: 10px 20px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(40, 8, 134);\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"    transition: background-color 0.3s, box-shadow 0.3s; /* add transition for background and box shadow */\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(82, 21, 252);\n"
"    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);\n"
"}")

        self.gridLayout.addWidget(self.btnOpenFile, 2, 0, 1, 1)

        self.btnRun = QPushButton(self.gridLayoutWidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"    padding: 10px 20px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(40, 8, 134);\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"    transition: background-color 0.3s, box-shadow 0.3s; /* add transition for background and box shadow */\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(82, 21, 252);\n"
"    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);\n"
"}")

        self.gridLayout.addWidget(self.btnRun, 2, 5, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"    display: inline-block;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.textFieldSearch = QTextEdit(self.gridLayoutWidget)
        self.textFieldSearch.setObjectName(u"textFieldSearch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textFieldSearch.sizePolicy().hasHeightForWidth())
        self.textFieldSearch.setSizePolicy(sizePolicy1)
        self.textFieldSearch.setStyleSheet(u"QTextEdit{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"background-color: #ffffff;\n"
"color:#282828;\n"
"border-radius: 15px;\n"
"border: 5px solid #280886\n"
"\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"border: 5px solid #5215fc;\n"
"}")

        self.gridLayout.addWidget(self.textFieldSearch, 2, 4, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"    display: inline-block;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.textFieldIgnore = QTextEdit(self.gridLayoutWidget)
        self.textFieldIgnore.setObjectName(u"textFieldIgnore")
        sizePolicy1.setHeightForWidth(self.textFieldIgnore.sizePolicy().hasHeightForWidth())
        self.textFieldIgnore.setSizePolicy(sizePolicy1)
        self.textFieldIgnore.setStyleSheet(u"QTextEdit{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"background-color: #ffffff;\n"
"color:#282828;\n"
"border-radius: 15px;\n"
"border: 5px solid #280886\n"
"\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"border: 5px solid #5215fc;\n"
"}")

        self.gridLayout.addWidget(self.textFieldIgnore, 2, 1, 1, 1)

        self.btnClear = QPushButton(self.gridLayoutWidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"    padding: 10px 20px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(40, 8, 134);\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"    transition: background-color 0.3s, box-shadow 0.3s; /* add transition for background and box shadow */\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(82, 21, 252);\n"
"    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);\n"
"}")

        self.gridLayout.addWidget(self.btnClear, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabMain, "")
        self.tabData = QWidget()
        self.tabData.setObjectName(u"tabData")
        self.tableView = QTableView(self.tabData)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 1211, 471))
        self.tableView.setStyleSheet(u"QTableView {\n"
"  background-color: #ffffff;\n"
"  color: #000000;\n"
"  font-family: Arial;\n"
"  font-size: 12pt;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"  border: 1px solid #dddddd;\n"
"  padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"  background-color: #dddddd;\n"
"}")
        self.tableView.setSortingEnabled(True)
        self.horizontalLayoutWidget = QWidget(self.tabData)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 570, 541, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGenRep = QPushButton(self.horizontalLayoutWidget)
        self.btnGenRep.setObjectName(u"btnGenRep")
        self.btnGenRep.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"    padding: 10px 20px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(40, 8, 134);\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"    transition: background-color 0.3s, box-shadow 0.3s; /* add transition for background and box shadow */\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(82, 21, 252);\n"
"    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);\n"
"}")

        self.horizontalLayout.addWidget(self.btnGenRep)

        self.btnDelRow = QPushButton(self.horizontalLayoutWidget)
        self.btnDelRow.setObjectName(u"btnDelRow")
        self.btnDelRow.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"    padding: 10px 20px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(40, 8, 134);\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
"     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"    transition: background-color 0.3s, box-shadow 0.3s; /* add transition for background and box shadow */\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(82, 21, 252);\n"
"    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);\n"
"}")

        self.horizontalLayout.addWidget(self.btnDelRow)

        self.tabWidget.addTab(self.tabData, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TextAnalizator", None))
        self.btnOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ignore", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), QCoreApplication.translate("MainWindow", u"Main", None))
        self.btnGenRep.setText(QCoreApplication.translate("MainWindow", u"Generate report", None))
        self.btnDelRow.setText(QCoreApplication.translate("MainWindow", u"Delete row", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QCoreApplication.translate("MainWindow", u"Data", None))
    # retranslateUi

