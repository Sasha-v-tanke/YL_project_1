# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatorBjMaZh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Categories = QTabWidget(self.centralwidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setGeometry(QRect(20, 30, 731, 560))
        self.Categories.setTabPosition(QTabWidget.North)
        self.Categories.setTabShape(QTabWidget.Triangular)
        self.Categories.setDocumentMode(False)
        self.Categories.setMovable(False)
        self.Categories.setTabBarAutoHide(True)
        self.BackToWelcome = QPushButton(self.centralwidget)
        self.BackToWelcome.setObjectName(u"BackToWelcome")
        self.BackToWelcome.setGeometry(QRect(10, 0, 75, 23))
        self.NewTab = QPushButton(self.centralwidget)
        self.NewTab.setObjectName(u"NewTab")
        self.NewTab.setGeometry(QRect(753, 30, 25, 25))
        self.ScrollBar = QScrollBar(self.centralwidget)
        self.ScrollBar.setObjectName(u"ScrollBar")
        self.ScrollBar.setGeometry(QRect(753, 60, 25, 525))
        self.ScrollBar.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Categories.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BackToWelcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0417\u0410\u0414", None))
        self.NewTab.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

