from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import csv
import re

class Register(QWidget):
    """
    注册界面
    """
    def __init__(self):
        super(Register, self).__init__()
        self.infoList = []
        self.initUi()

    def initUi(self):
        self.setWindowTitle("注册")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 300)

        subLayout = QGridLayout()

        lable1 = QLabel("用户名:")
        label2 = QLabel("密码:")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("请输入你的用户名")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("请输入你的密码")

        self.okButton = QPushButton("确认")
        self.okButton.clicked.connect(self.okButtonClicker)
        self.okButton.clicked.connect(self.close)
        self.cancelButton = QPushButton("取消")
        self.cancelButton.clicked.connect(self.close)

        subLayout.addWidget(lable1, 0, 0)
        subLayout.addWidget(self.lineEdit1, 0, 1)
        subLayout.addWidget(label2, 1, 0)
        subLayout.addWidget(self.lineEdit2, 1, 1)
        subLayout.addWidget(self.okButton, 2, 0)
        subLayout.addWidget(self.cancelButton, 2, 1)

        self.setLayout(subLayout)

    def okButtonClicker(self):
        QMessageBox.information(self, "Information", "注册成功啦!")
        userName = self.lineEdit1.text()
        password = self.lineEdit2.text()
        userInfo = str(userName) + ',' + str(password) + '\n'
        with open("E:/PycharmProject/SE/database/usersList.txt", "a") as f:
            f.write(userInfo)