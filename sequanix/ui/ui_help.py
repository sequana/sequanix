# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Help(object):
    def setupUi(self, Help):
        if not Help.objectName():
            Help.setObjectName(u"Help")
        Help.resize(456, 582)
        self.gridLayout = QGridLayout(Help)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Help)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(Help)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Help)

        QMetaObject.connectSlotsByName(Help)
    # setupUi

    def retranslateUi(self, Help):
        Help.setWindowTitle(QCoreApplication.translate("Help", u"Sequana Help", None))
    # retranslateUi

