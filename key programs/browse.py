from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import csv
import sys


class BrowsePage(QWidget):
    """
    查看商品信息模块
    """
    def __init__(self):
        super(BrowsePage,self).__init__()
        self.initUI()

    def browseinfo(self, i):
        self.check = browseInfo(i)
        self.check.show()

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

        button1 = QPushButton("查看具体信息")
        button1.clicked.connect(lambda: self.browseinfo(0))
        mainLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("查看具体信息")
        button2.clicked.connect(lambda: self.browseinfo(1))
        mainLayout.addWidget(button2, 1, 1)

        button3 = QPushButton("查看具体信息")
        button3.clicked.connect(lambda: self.browseinfo(2))
        mainLayout.addWidget(button3, 2, 1)

        button4 = QPushButton("查看具体信息")
        button4.clicked.connect(lambda: self.browseinfo(3))
        mainLayout.addWidget(button4, 3, 1)

        button5 = QPushButton("查看具体信息")
        button5.clicked.connect(lambda: self.browseinfo(4))
        mainLayout.addWidget(button5, 4, 1)

        button6 = QPushButton("查看具体信息")
        button6.clicked.connect(lambda: self.browseinfo(5))
        mainLayout.addWidget(button6, 5, 1)

        self.setLayout(mainLayout)

class browseInfo(QWidget):
    """
    商品信息栏
    """
    def __init__(self, id=0):
        super(browseInfo,self).__init__()
        self.id = id
        self.initUi()

    def initUi(self):
        self.createGridGroupBox()
        self.creatVboxGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout.addStretch()
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addWidget(self.vboxGroupBox)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setLayout(mainLayout)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("基本信息栏")
        layout = QGridLayout()
        self.label = QLabel()
        filepath = 'E:/PycharmProject/SE/itemsList/' + str(self.id + 1) + '.txt'
        with open(filepath, "r") as f:
            lines = f.readlines()
            length = len(lines)
            if length == 5:
                for j in range(len(lines) - 1):
                    line = lines[j].split('\n')[0]
                    label = QLabel(line)
                    layout.addWidget(label, j, 0)
            else:
                for j in range(len(lines) - 2):
                    line = lines[j].split('\n')[0]
                    label = QLabel(line)
                    layout.addWidget(label, j, 0)
        self.gridGroupBox.setLayout(layout)
        self.setWindowTitle('商品信息')

    def creatVboxGroupBox(self):
        self.vboxGroupBox = QGroupBox("商品图片栏")
        layout = QVBoxLayout()
        label = QLabel()
        imagePath = 'E:/PycharmProject/SE/imagesList/' + str(self.id + 1) + '.png'
        pix = QPixmap(imagePath)

        scaredPixmap = pix.scaled(QSize(300, 300), aspectRatioMode=Qt.KeepAspectRatio)
        label.setPixmap(scaredPixmap)
        layout.addWidget(label)
        self.vboxGroupBox.setLayout(layout)

    def creatFormGroupBox(self):
        self.formGroupBox = QGroupBox("商品描述栏")
        layout = QFormLayout()
        performanceLabel = QLabel("商品具体描述：")
        filepath = 'E:/PycharmProject/SE/itemsList/' + str(self.id + 1) + '.txt'
        with open(filepath, "r") as f:
            lines = f.readlines()
            length = len(lines)
            if length == 5:
                line = lines[-1].split(':')[1].split('\n')[0]
            else:
                line = lines[length-2].split(':')[1].split('\n')[0]
            performanceEditor = QLabel(line)
            performanceEditor.setWordWrap(True)

        layout.addRow(performanceLabel,performanceEditor)

        self.formGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrowsePage()
    ex.show()
    sys.exit(app.exec_())
