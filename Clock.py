#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class clock(QWidget):
    
  #constructor
  def __init__(self):
        
        super().__init__()
        
        # creating a timer object
        timer=QTimer(self)
        
        #add action to timer
        #update the code each time
        timer.timeout.connect(self.update)
        
        #set the timer to be at 1sec i.e 1000
        timer.start(1000)
        #Set the title of the window
        self.setWindowTitle("Clock")
        #Set the window size
        self.setGeometry(200,200,300,300)
        #Set the background color
        self.setStyleSheet("background:black;")
        #Creating hands of clock
        #Creating Hour Hand
        self.hPointer=QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-50)])
        #Creating Minute Hand
        self.mPointer=QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])
        #Creating Sec Hand
        self.sPointer=QtGui.QPolygon([QPoint(1,1),QPoint(-1,1),QPoint(0,-90)])
    
        #Setting colors for hands
        self.hColor=Qt.red
        self.mColor=Qt.red
        self.sColor=Qt.yellow

      #paint method used to set minimum and maximum of height and width of clock.
  def paintEvent(self, event):
        rec = min(self.width(), self.height())
        #Get Current Time.
        curr = QTime.currentTime()
        # creating a painter object
        painter = QPainter(self)
        # method to draw the hands
        # arguments : color and which hand should be pointed
        def drawPointer(color, rotation, pointer):
          # setting brush
          painter.setBrush(QBrush(color))
          # saving painter
          painter.save()
          # rotating painter
          painter.rotate(rotation)
          # draw the hand
          painter.drawConvexPolygon(pointer)
          # restore the painter
          painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)
        # scale the painter
        painter.scale(rec / 200, rec / 200)
        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)

        #Draw Hands of Clock
        drawPointer(self.hColor, (30 * (curr.hour() + curr.minute() / 60)), self.hPointer)
        drawPointer(self.mColor, (6 * (curr.minute() + curr.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * curr.second()), self.sPointer)

        # drawing background
        painter.setPen(QPen(self.hColor))
        for i in range(0, 60):
          #Drawing Background
          if (i % 5) == 0:
            painter.drawLine(87, 0, 97, 0)
          # rotating the painter
          painter.rotate(6)
        painter.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # creating a clock object
    win = clock()
    # show
    win.show()
    sys.exit(app.exec_())  




