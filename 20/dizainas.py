# Form implementation generated from reading ui file 'D:\PYTON\pirma_aplikacija\20\programa.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 265)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(20, 80, 171, 101))
        self.minus.setObjectName("minus")
        self.plius = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plius.setGeometry(QtCore.QRect(380, 80, 171, 101))
        self.plius.setObjectName("plius")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 120, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.zodis = QtWidgets.QLabel(parent=self.centralwidget)
        self.zodis.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.zodis.setObjectName("zodis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plius.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "0"))
        self.zodis.setText(_translate("MainWindow", " "))
