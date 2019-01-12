from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
import os

from release import ReleasePage
from browse import BrowsePage
from update import UpdatePage

class PublishPage(QWidget):
    """
    商品管理界面
    """
    def __init__(self):
        super(PublishPage,self).__init__()
        self.initUI()

    def Publish(self):
        self.publish = ReleasePage()
        self.publish.show()
    def Browse(self):
        self.browse = BrowsePage()
        self.browse.show()
    def Update(self):
        self.update = UpdatePage()
        self.update.show()

    def initUI(self):
        self.setWindowTitle("商品管理")
        self.setWindowIcon(QIcon('E:/PycharmProject/SE/database/logo.jpg'))
        self.setGeometry(400, 400, 300, 260)

        self.publishButton = QPushButton(self)
        self.publishButton.setText("发布商品信息")
        self.publishButton.clicked.connect(self.newTxt)
        self.publishButton.clicked.connect(self.Publish)
        self.publishButton.setToolTip("点击发布商品信息")
        self.publishButton.move(100, 50)

        self.browseButton = QPushButton(self)
        self.browseButton.setText("查看我的商品")
        self.browseButton.clicked.connect(self.Browse)
        self.browseButton.setToolTip("点击查看商品信息")
        self.browseButton.move(100, 100)

        self.updateButton = QPushButton(self)
        self.updateButton.setText("更新商品信息")
        self.updateButton.clicked.connect(self.Update)
        self.updateButton.setToolTip("点击更新商品信息")
        self.updateButton.move(100, 150)


    def newTxt(self):
        path = 'E:/PycharmProject/SE/itemsList'
        itemList = os.listdir(path)
        if len(itemList):
            numofitem = len(itemList)
            maxnum = itemList[numofitem - 1].split(".")[0]
            filepath = path + '/' + str(int(maxnum) + 1) + '.txt'
            f = open(filepath, 'w')
            f.close()
        else:
            maxnum = 0
            filepath = path + '/' + str(maxnum + 1) + '.txt'
            f = open(filepath, 'w')
            f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PublishPage()
    ex.show()
    sys.exit(app.exec_())
