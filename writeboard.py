#手写数字画板的实现

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QSize

class WriteBoard(QWidget):
    def __init__(self, Parent = None,Size = QSize(400, 400), Fill = QColor(255,255,255,255)):
        super().__init__(Parent)

        #初始化画板参数
        self.__size = Size                      #使用一个私有变量来保存画板尺寸
        self.__fill = Fill                      #画板默认填充颜色

        self.__thickness = 10                   #默认画笔粗细
        self.__penColor = QColor(0,0,0,255)     #默认画笔颜色

        self.__begin_point = QPoint()
        self.__end_point = QPoint()
        
        # 初始化画板界面
        self.__board = QPixmap(self.__size)
        self.__board.fill(Fill) 
        self.setFixedSize(self.__size)          
        self.__painter = QPainter()             # 新建绘图工具

    #清空画板
    def Clear(self):
        self.__board.fill(self.__fill)
        #update后调用paintEvent()函数进行绘制
        self.update()
    
    #填充画板
    def setBoardFill(self,fill):
        self.__fill = fill
        self.__board.fill(self.__fill)
        #update后调用paintEvent()函数进行绘制
        self.update()

    #设置画笔粗细
    def setPenThickness(self,thickness):
        self.__thickness = thickness

    #设置画笔颜色
    def setPenColor(self,color):
        self.__penColor = color

    # 获取画板QImage类型图片
    def getContentAsQImage(self):
        image = self.__board.toImage()
        return image 

    # 绘图事件响应，update()后调用此函数
    def paintEvent(self, paintEvent):         
        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()

    # 鼠标按下事件响应
    def mousePressEvent(self, mouseEvent):
        if mouseEvent.button() == Qt.LeftButton:
            self.__begin_point = mouseEvent.pos()
            self.__end_point = self.__begin_point
            #update后调用paintEvent()函数进行绘制
            self.update()


    #鼠标移动事件响应
    def mouseMoveEvent(self, mouseEvent):
        if mouseEvent.buttons() == Qt.LeftButton:
            self.__end_point = mouseEvent.pos()

            # 画入缓冲区
            self.__painter.begin(self.__board)

            #设置画笔粗细 颜色
            self.__painter.setPen(QPen(self.__penColor,self.__thickness))

            # 根据鼠标指针前后两个位置绘制直线
            self.__painter.drawLine(self.__begin_point, self.__end_point)
            self.__painter.end()

            # 让前一个坐标值等于后一个坐标值，
		    # 这样就能实现画出连续的线
            self.__begin_point = self.__end_point
            
            #update后调用paintEvent()函数进行绘制
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WriteBoard()
    demo.show()
    sys.exit(app.exec_())