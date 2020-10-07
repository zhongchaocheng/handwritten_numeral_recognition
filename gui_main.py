#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
import numpy as np
from getFeature import GetFeature


from Ui_layout import Ui_Dialog
from writeboard import WriteBoard

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton, QFrame
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QImage
from PyQt5.QtCore import Qt, QPoint, QSize


from PIL import Image, ImageQt

MODE_MNIST = 1    # MNIST随机抽取
MODE_WRITE = 2    # 手写输入




class MainWindow(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(MainWindow,self).__init__()
    
        # 初始化参数
        self.mode = MODE_MNIST
  
        # 初始化UI
        self.setupUi(self)
        self.center()

        # 初始化画板
        self.writeBoard = WriteBoard(self, Size = QSize(32, 32), Fill = QColor(0,0,0,0))
        self.writeBoard.setPenColor(QColor(0,0,0,0))
        self.dAreaLayout.addWidget(self.writeBoard)

        self.clearDataArea()
        self.init()

    def init(self):
        self.mode = MODE_MNIST
        # 更改背景
        self.writeBoard.setBoardFill(QColor(255,255,255,255))      
        self.writeBoard.setPenColor(QColor(0,0,0,255)) 


    # 窗口居中
    def center(self):
        # 获得窗口
        framePos = self.frameGeometry()
        # 获得屏幕中心点
        scPos = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        framePos.moveCenter(scPos)
        self.move(framePos.topLeft())
    
    
    # 窗口关闭事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
    
    # 清除数据待输入区
    def clearDataArea(self):
        self.writeBoard.Clear()
 



    #透明  QColor(0,0,0,0)
    #黑色  QColor(0,0,0,255)
    #白色  QColor(255,255,255,255)
    def mode_change_callback(self, text):

        if text == '1.训练模式':
            self.mode = MODE_MNIST
            self.clearDataArea()
            # 更改背景
            self.writeBoard.setBoardFill(QColor(255,255,255,255))      
            self.writeBoard.setPenColor(QColor(0,0,0,255)) 
            #print('训练模式')

        if text == '2.手写识别模式':
            self.mode = MODE_WRITE
            self.clearDataArea()
            # 更改背景
            self.writeBoard.setBoardFill(QColor(255,255,255,255))      
            self.writeBoard.setPenColor(QColor(0,0,0,255)) 

            #print('手写模式')

    def save_clicked_callback(self):
        image = self.writeBoard.getContentAsQImage()
        # 转换成pil image类型处理
        pil_img = ImageQt.fromqimage(image)
        #pil_img = pil_img.resize((28, 28), Image.ANTIALIAS)
        print(pil_img.size)
        #pil_img.save('test.png')
        #pil_img = pil_img.convert('1')
        
        GetFeature(pil_img)
        
        # img_array = np.where(img_array>0.5, 1, 0)



    def clear_clicked_callback(self):
        self.clearDataArea()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Gui = MainWindow()
    Gui.show()
    sys.exit(app.exec_())