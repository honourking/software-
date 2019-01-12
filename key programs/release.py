from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import csv
import cv2


class ReleasePage(QWidget):
    """
    商品发布模块
    """
    def __init__(self):
        super(ReleasePage,self).__init__()
        self.infoList = []
        self.initUi()

    def initUi(self):
        """
        窗口基本布局设置
        :return:
        """
        self.setWindowTitle("商品信息")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 400)

        label1=QLabel("商品名称:")
        label2=QLabel("商品标签:")
        label3=QLabel("商品价格:")
        label4=QLabel("你的微信:")
        label5=QLabel("商品介绍:")

        self.nameLable = QLabel("你的商品名字")
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.styleLable = QLabel("生活用品")
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.numberLable = QLabel("100.0")
        self.numberLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.costLable = QLabel("请输入你的微信")
        self.costLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.introductionLable = QLabel("请介绍你的商品")
        self.introductionLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

        nameButton=QPushButton("...")
        nameButton.clicked.connect(self.selectName)
        styleButton=QPushButton("...")
        styleButton.clicked.connect(self.selectLable)
        numberButton=QPushButton("...")
        numberButton.clicked.connect(self.selectPrice)
        costButton=QPushButton("...")
        costButton.clicked.connect(self.selectContact)
        introductionButton=QPushButton("...")
        introductionButton.clicked.connect(self.selectIntroduction)
        uploadButton=QPushButton("上传商品图片")
        uploadButton.clicked.connect(self.Upload)

        ensureButton = QPushButton("OK")
        ensureButton.clicked.connect(self.ensurebuttonClicked)
        ensureButton.clicked.connect(self.close)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        cancelButton.clicked.connect(self.cancelButtonClicker)

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.nameLable,0,1)
        mainLayout.addWidget(nameButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.styleLable,1,1)
        mainLayout.addWidget(styleButton,1,2)
        mainLayout.addWidget(label3,2,0)
        mainLayout.addWidget(self.numberLable,2,1)
        mainLayout.addWidget(numberButton,2,2)
        mainLayout.addWidget(label4,3,0)
        mainLayout.addWidget(self.costLable,3,1)
        mainLayout.addWidget(costButton,3,2)
        mainLayout.addWidget(label5,4,0)
        mainLayout.addWidget(self.introductionLable,4,1)
        mainLayout.addWidget(introductionButton,4,2)
        mainLayout.addWidget(uploadButton, 5, 1)
        mainLayout.addWidget(ensureButton, 6, 1)
        mainLayout.addWidget(cancelButton, 6, 2)

        self.setLayout(mainLayout)

    def Upload(self):
        """
        调用上传图片模块
        :return:
        """
        self.upload = UploadImage()
        self.upload.show()

    def selectName(self):
        """
        商品名称设置
        :return:
        """
        name,ok = QInputDialog.getText(self,"商品名称","输入商品名称:",
                                       QLineEdit.Normal,self.nameLable.text())

        if ok and (len(name)!=0):
            self.nameLable.setText(name)
            nameob = "商品名称:" + name + "\n"
            self.infoList.append(nameob)

    def selectLable(self):
        """
        商品标签设置
        :return:
        """
        list = ["生活用品","体育用品","电子产品","服装穿戴","美容美妆"]

        style,ok = QInputDialog.getItem(self,"商品标签","请选择商品标签:",list)
        if ok :
            self.styleLable.setText(style)

            styleob = "商品标签:" + style + "\n"

            self.infoList.append(styleob)

    def selectPrice(self):
        """
        商品价格设置
        :return:
        """
        number, ok = QInputDialog.getDouble(self, "商品价格", "请输入商品定价:",
                                            float(self.numberLable.text()), 0.0, 10000.0, 1)
        if ok :
            self.numberLable.setText(str(number))
            numberob = "商品价格:" + str(number) + "\n"
            self.infoList.append(numberob)

    def selectContact(self):
        """
        卖家联系方式设置
        :return:
        """
        cost,ok = QInputDialog.getText(self,"你的微信", "请输入的微信:",
                                       QLineEdit.Normal,self.costLable.text())
        if ok :
            self.costLable.setText(str(cost))

            costob = "你的微信:" + cost + "\n"
            self.infoList.append(costob)

    def selectIntroduction(self):
        """
        商品具体描述设置
        :return:
        """
        introduction,ok = QInputDialog.getMultiLineText(self,"商品介绍","介绍:", "我的商品无敌")
        if ok :
            self.introductionLable.setText(introduction)

            introductionob = "商品介绍:" + introduction + "\n"
            self.infoList.append(introductionob)

    def ensurebuttonClicked(self):
        QMessageBox.information(self, "Information", "商品发布成功")
        path = 'E:/PycharmProject/SE/itemsList'
        itemList = os.listdir(path)
        numofitem = len(itemList)
        maxnum = itemList[numofitem - 1].split(".")[0]
        filepath = path + '/' + maxnum + '.txt'
        with open(filepath, 'w') as f:
            for i in range(len(self.infoList)):
                f.write(self.infoList[i])

        newItem = [maxnum + '.txt' + ',', self.infoList[0].split(':')[1]]
        with open("E:/PycharmProject/SE/database/itemsName.txt", "a") as f:
            f.writelines(newItem)


    def cancelButtonClicker(self):
        path = 'E:/PycharmProject/SE/itemsList'
        itemList = os.listdir(path)
        numofitem = len(itemList)
        maxnum = itemList[numofitem - 1].split(".")[0]
        filepath = path + '/' + maxnum + '.txt'
        os.remove(filepath)

class UploadImage(QWidget):
    """
    上传商品照片模块
    """

    def __init__(self, parent=None):
        super(UploadImage, self).__init__(parent)
        self.filePath = []

        self.setWindowTitle("上传图片")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 100)
        layout = QVBoxLayout()

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("从文件中获取照片")
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.OkButton)
        self.btn_2.clicked.connect(self.close)
        self.btn_2.setText("确认")
        layout.addWidget(self.btn_2)

        self.setWindowTitle("上传商品图片")

        self.setLayout(layout)

    def loadFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        if fname:
            self.filePath.append(fname)
            pixmap = QPixmap(fname)
            scaredPixmap = pixmap.scaled(400,400,aspectRatioMode=Qt.KeepAspectRatio)
            self.label.setPixmap(scaredPixmap)

    def OkButton(self):
        QMessageBox.information(self, "Information", "图片上传成功")
        path = self.filePath[0]
        imagePath = 'E:/PycharmProject/SE/imagesList'
        imageList = os.listdir(imagePath)
        numofimage = len(imageList)
        if numofimage:
            maxnum = imageList[numofimage - 1].split(".")[0]
            savePath = imagePath + '/' + str(int(maxnum)+1) + '.png'
        else:
            savePath = imagePath + '/' + '1.png'

        image = cv2.imread(path)
        cv2.imwrite(savePath, image)


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=ReleasePage()
    myshow.show()
    sys.exit(app.exec_())

