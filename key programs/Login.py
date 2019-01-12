from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

import Mainpage
from Register import Register

class Login_Window(QtWidgets.QMainWindow):
    """
    登陆界面
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 357)
        MainWindow.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        MainWindow.setStyleSheet("background-image:url(E:/PycharmProject/SE/database/background.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(600, 100, 150, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 140, 150, 30))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(500, 100, 70, 30))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setFont(QFont("Roman times",20))

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(500, 140, 70, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QFont("Roman times",20))

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 200, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 200, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "西电二手交易平台"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))

        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton.setFont(QFont("Roman times",10))
        self.pushButton.clicked.connect(self.word_get)

        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.setFont(QFont("Roman times", 10))
        self.pushButton_2.clicked.connect(self.register)

    def register(self):
        self.reg = Register()
        self.reg.show()

    def word_get(self):
        input_userName = self.lineEdit.text()
        input_password = self.lineEdit_2.text()
        flag = 0
        with open("E:/PycharmProject/SE/database/usersList.txt", "r") as f:
            infoList = f.readlines()
            for i in range(len(infoList)):
                userName = infoList[i].split(',')[0]
                password = infoList[i].split(',')[1].split()[0]
                if str(input_userName) == userName and str(input_password) == password:
                    flag = 1
                    break

        if flag:
            mainInterface.show()
            MainWindow.close()
        else:
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login_Window()
    mainInterface = Mainpage.MainInterface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())