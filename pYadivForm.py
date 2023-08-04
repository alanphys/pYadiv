# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pYadivForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import pYadivForm_rc

class Ui_pYadivForm(object):
    def setupUi(self, pYadivForm):
        if not pYadivForm.objectName():
            pYadivForm.setObjectName(u"pYadivForm")
        pYadivForm.resize(528, 605)
        pYadivForm.setAcceptDrops(True)
        pYadivForm.setIconSize(QSize(32, 32))
        self.actionOpen = QAction(pYadivForm)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/Images/Icons/ImageOpen.xpm", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionExit = QAction(pYadivForm)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Icons/exit.xpm", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionAbout = QAction(pYadivForm)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionInvert = QAction(pYadivForm)
        self.actionInvert.setObjectName(u"actionInvert")
        icon2 = QIcon()
        icon2.addFile(u":/Images/Icons/invert.xpm", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInvert.setIcon(icon2)
        self.actionAuto_Window = QAction(pYadivForm)
        self.actionAuto_Window.setObjectName(u"actionAuto_Window")
        icon3 = QIcon()
        icon3.addFile(u":/Images/Icons/window.xpm", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAuto_Window.setIcon(icon3)
        self.centralwidget = QWidget(pYadivForm)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.qlImage = QLabel(self.centralwidget)
        self.qlImage.setObjectName(u"qlImage")
        sizePolicy.setHeightForWidth(self.qlImage.sizePolicy().hasHeightForWidth())
        self.qlImage.setSizePolicy(sizePolicy)
        self.qlImage.setAcceptDrops(True)
        self.qlImage.setScaledContents(False)

        self.gridLayout.addWidget(self.qlImage, 0, 0, 1, 1)

        pYadivForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pYadivForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 30))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        pYadivForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pYadivForm)
        self.statusbar.setObjectName(u"statusbar")
        pYadivForm.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(pYadivForm)
        self.toolBar.setObjectName(u"toolBar")
        pYadivForm.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionInvert)
        self.menuTools.addAction(self.actionAuto_Window)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInvert)
        self.toolBar.addAction(self.actionAuto_Window)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(pYadivForm)
        self.actionExit.triggered.connect(pYadivForm.close)

        QMetaObject.connectSlotsByName(pYadivForm)
    # setupUi

    def retranslateUi(self, pYadivForm):
        pYadivForm.setWindowTitle(QCoreApplication.translate("pYadivForm", u"pYadiv Form", None))
        self.actionOpen.setText(QCoreApplication.translate("pYadivForm", u"&Open", None))
        self.actionExit.setText(QCoreApplication.translate("pYadivForm", u"E&xit", None))
        self.actionAbout.setText(QCoreApplication.translate("pYadivForm", u"&About", None))
        self.actionInvert.setText(QCoreApplication.translate("pYadivForm", u"&Invert", None))
        self.actionAuto_Window.setText(QCoreApplication.translate("pYadivForm", u"Auto &Window", None))
        self.qlImage.setText("")
        self.menu_File.setTitle(QCoreApplication.translate("pYadivForm", u"Fi&le", None))
        self.menu_Help.setTitle(QCoreApplication.translate("pYadivForm", u"&Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("pYadivForm", u"&Tools", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("pYadivForm", u"toolBar", None))
    # retranslateUi

