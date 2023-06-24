from PySide2.QtWidgets import  *
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2 import QtGui,QtCore,QtWidgets
from PySide2.QtGui import *

import cv2
import sys, os
import PySide2
import firstSource
import secondSource

from MyControl import *
"""
测试
"""
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Status:
    def __init__(self):
        self.ui = QUiLoader().load('ui/pedestrian_double_photo_working.ui')
        self.listWidget = QListWidget(self.ui)
        self.listWidget.setStyleSheet("""QListWidget{border:0px;}QListWidget:item{margin:10px 0px 10px 0px;}""")
        for i in range(5):
            self.listWidget.move(1322, 358 + 16 + 36)
            self.listWidget.resize(370, 540 - 16 - 40)
            item=QListWidgetItem()
            self.listWidget.addItem(item)
            item.setSizeHint(QSize(330,70))
            widget=QWidget()
            widget.resize(330,70)
            label1=double_photo_show_label(widget,0,"source/second/menu_car.PNG"
                                           ,10,0,100,70)
            label2 = double_photo_show_label(widget, 0, "source/second/menu_car.PNG"
                                             , 126, 0, 100, 70)
            label3 = double_photo_show_label(widget, 1, 100
                                             , 242, 17, 98, 36)
            self.listWidget.setItemWidget(item,widget)

        print(self.ui.listWidget.count())
        self.ui.show()

if __name__ == '__main__':
    app = QApplication([])
    MainWindow=QMainWindow()
    statu = Status()
    statu.ui.show()
    app.exec_()
