from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import csv
import re

from browse import browseInfo

class SearchInterface(QtWidgets.QMainWindow):
    """
    搜索界面
    """
    def __init__(self):
        super(SearchInterface, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        MainWindow.resize(386, 200)
        # MainWindow.setWindowIcon(QIcon('logo.png'))
        # MainWindow.setStyleSheet("background-image:url(Background.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 150, 25))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(75, 70, 75, 25))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "商品搜索"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入商品名称"))
        self.label.setText(_translate("MainWindow", "商品名称"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))

    def searchResult(self, id):
        self.result = browseInfo(id)
        self.result.show()

    def word_get(self):
        pattern = self.lineEdit.text()

        flag = 0
        with open('E:/PycharmProject/SE/database/itemsName.txt', 'r') as f:
            itemsList = f.readlines()

            for i in range(len(itemsList)):
                itemPath = itemsList[i].split(',')[0].split('.')[0]
                itemName = itemsList[i].split(',')[1].split()[0]

                itemList = []
                itemList.append(int(itemPath))
                itemList.append(itemName)
                if re.search(pattern, itemName, flags=0):
                    flag = 1
                    break

        if flag:
            id = int(itemPath) - 1
            self.searchResult(id)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "好气呀，啥都没找到!",
                                QMessageBox.Yes)

