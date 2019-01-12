from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Searchpage import SearchInterface
from PublishPage import PublishPage

class MainInterface(QtWidgets.QMainWindow):
    """
    主界面
    """
    def __init__(self):
        super(MainInterface,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 150, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word1_get)

        self.pushButton_2.clicked.connect(self.goodsPublish)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "西电二手交易平台"))
        self.pushButton.setText(_translate("MainWindow", "商品搜索"))
        self.pushButton_2.setText(_translate("MainWindow", "商品管理"))

    def goodsPublish(self):
        self.publish = PublishPage()
        self.publish.show()

    def searchShow(self):
        self.searchInter = SearchInterface()
        self.searchInter.show()

    def word1_get(self):
        self.searchShow()

