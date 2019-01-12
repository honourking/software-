from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import csv
import sys

class UpdateInfo(QWidget):
    """
    修改商品信息模块
    """
    def __init__(self, id):
        super(UpdateInfo,self).__init__()
        self.id = id
        self.infoList = []
        self.initUi()

    def initUi(self):
        self.setWindowTitle("商品信息")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 400)

        label1 = QLabel("商品名称:")
        label2 = QLabel("商品标签:")
        label3 = QLabel("商品价格:")
        label4 = QLabel("你的微信:")
        label5 = QLabel("商品介绍:")

        self.nameLable = QLabel("你的商品名字")
        self.nameLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.styleLable = QLabel("生活用品")
        self.styleLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.numberLable = QLabel("100.0")
        self.numberLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.costLable = QLabel("请输入你的微信")
        self.costLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.introductionLable = QLabel("请介绍你的商品")
        self.introductionLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        nameButton = QPushButton("修改")
        nameButton.clicked.connect(self.selectName)
        styleButton = QPushButton("修改")
        styleButton.clicked.connect(self.selectLabel)
        numberButton = QPushButton("修改")
        numberButton.clicked.connect(self.selectPrice)
        costButton = QPushButton("修改")
        costButton.clicked.connect(self.selectContact)
        introductionButton = QPushButton("修改")
        introductionButton.clicked.connect(self.selectIntroduction)
        # ensureButton=QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        ensureButton = QPushButton("OK")
        ensureButton.clicked.connect(self.ensurebuttonClicked)
        ensureButton.clicked.connect(self.close)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        cancelButton.clicked.connect(self.cancelButtonClicker)

        mainLayout = QGridLayout()
        mainLayout.addWidget(label1, 0, 0)
        mainLayout.addWidget(self.nameLable, 0, 1)
        mainLayout.addWidget(nameButton, 0, 2)
        mainLayout.addWidget(label2, 1, 0)
        mainLayout.addWidget(self.styleLable, 1, 1)
        mainLayout.addWidget(styleButton, 1, 2)
        mainLayout.addWidget(label3, 2, 0)
        mainLayout.addWidget(self.numberLable, 2, 1)
        mainLayout.addWidget(numberButton, 2, 2)
        mainLayout.addWidget(label4, 3, 0)
        mainLayout.addWidget(self.costLable, 3, 1)
        mainLayout.addWidget(costButton, 3, 2)
        mainLayout.addWidget(label5, 4, 0)
        mainLayout.addWidget(self.introductionLable, 4, 1)
        mainLayout.addWidget(introductionButton, 4, 2)
        # mainLayout.addWidget((ensureButton,4,2))
        mainLayout.addWidget(ensureButton, 5, 1)
        mainLayout.addWidget(cancelButton, 5, 2)

        self.setLayout(mainLayout)

    def selectName(self):
        name, ok = QInputDialog.getText(self, "商品名称", "输入商品名称:",
                                        QLineEdit.Normal, self.nameLable.text())

        if ok and (len(name) != 0):
            self.nameLable.setText(name)
            nameob = "商品名称:" + name + "\n"
            self.infoList.append(nameob)

    def selectLabel(self):
        list = ["生活用品", "体育用品", "电子产品", "服装穿戴", "美容美妆"]

        style, ok = QInputDialog.getItem(self, "商品标签", "请选择商品标签:", list)
        if ok:
            self.styleLable.setText(style)

            styleob = "商品标签:" + style + "\n"

            self.infoList.append(styleob)

    def selectPrice(self):
        number, ok = QInputDialog.getDouble(self, "商品价格", "请输入商品定价:",
                                            float(self.numberLable.text()), 0.0, 10000.0, 1)
        if ok:
            self.numberLable.setText(str(number))
            numberob = "商品价格:" + str(number) + "\n"
            self.infoList.append(numberob)

    def selectContact(self):
        cost, ok = QInputDialog.getText(self, "你的微信", "请输入你的微信:",
                                        QLineEdit.Normal, self.costLable.text())
        if ok:
            self.costLable.setText(str(cost))

            costob = "你的微信:" + cost + "\n"
            self.infoList.append(costob)

    def selectIntroduction(self):
        introduction, ok = QInputDialog.getMultiLineText(self, "商品介绍", "介绍:", "我的商品无敌")
        if ok:
            self.introductionLable.setText(introduction)

            introductionob = "商品介绍:" + introduction + "\n"
            self.infoList.append(introductionob)

    def ensurebuttonClicked(self):
        QMessageBox.information(self, "通知", "信息修改成功")
        path = 'E:/PycharmProject/SE/itemsList/' + str(self.id) + '.txt'
        with open(path, "w") as f:
            for j in range(len(self.infoList)):
                f.write(self.infoList[j])

    def cancelButtonClicker(self):
        path = 'E:/PycharmProject/SE/itemsList'
        itemList = os.listdir(path)
        numofitem = len(itemList)
        maxnum = itemList[numofitem - 1].split(".")[0]
        filepath = path + '/' + maxnum + '.txt'
        os.remove(filepath)


class UpdatePage(QWidget):
    """
    商品列表模块
    """
    def __init__(self):
        super(UpdatePage, self).__init__()
        self.initUI()

    def updateinfo(self, id):
        self.update = UpdateInfo(id)
        self.update.show()

    def initUI(self):
        self.setWindowTitle("我发布的商品")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 500)

        mainLayout = QGridLayout()

        with open("E:/PycharmProject/SE/database/itemsName.txt", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                name = lines[i].split(',')[1].split()[0]
                label = QLabel(name)
                mainLayout.addWidget(label, i, 0)

        button1 = QPushButton("修改")
        button1.clicked.connect(lambda: self.updateinfo(1))
        mainLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("修改")
        button2.clicked.connect(lambda: self.updateinfo(2))
        mainLayout.addWidget(button2, 1, 1)

        button3 = QPushButton("修改")
        button3.clicked.connect(lambda: self.updateinfo(2))
        mainLayout.addWidget(button3, 2, 1)

        button4 = QPushButton("修改")
        button4.clicked.connect(lambda: self.updateinfo(3))
        mainLayout.addWidget(button4, 3, 1)

        button5 = QPushButton("修改")
        button5.clicked.connect(lambda: self.updateinfo(4))
        mainLayout.addWidget(button5, 4, 1)

        button6 = QPushButton("修改")
        button6.clicked.connect(lambda: self.updateinfo(5))
        mainLayout.addWidget(button6, 5, 1)

        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UpdatePage()
    ex.show()
    sys.exit(app.exec_())
