import time
import os
from PyQt5.QtCore import QCoreApplication, QMimeData, QTimer
import mouse
import threading 
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal

#import script


class Count():
    count = 0 
class MyWindow(QMainWindow, threading.Thread, Count):
    count = 0


    def __init__(self):
        super(MyWindow, self).__init__()
        self.thread = threading.Thread(target=self.inc)
        self.threadLock = threading.Lock()
        self.setStyleSheet("background-color: #202A44;")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("Primogem Counter")
        self.initUI()
    

    

    

    def update_primos(self, primos):
        f = open('/Users/vmoda/Project/text.txt','w')
        f.write(str(primos))
    
    def getPrimos(self):
        f = open('/Users/vmoda/Project/text.txt', "r")
        for x in f:
            return x
    
    
    def pauseCount(self, num):
        self.count += 1
        global exit
        if self.count % 2 != 0:
            exit = 2
            self.stop.setText('Resume')
        elif self.count % 2 == 0:
            exit = 3
            self.stop.setText('Pause')
            self.threadLock.release()  
            




    def exit(self):
        global exit 
        exit = 1
       
    def inc(self):
        print("running")
        file = open('/Users/vmoda/Project/text.txt', 'r')
        for x in file:
           primos = int(x)
           file.close
        global exit
        exit = 0
        while (True): 
            if exit == 1:
                time.sleep(10000)
                break
            elif exit == 2:
                self.threadLock.acquire()
            else:
                time.sleep(0.01)
                primos += 10    
                self.update_primos(primos)
                self.primos.setText(self.getPrimos())
                self.primos.adjustSize()
               
        
    def hidebutton(self):
        self.thread.start()
        self.b.hide()
    
   

    def initUI(self):

        self.menu = QtWidgets.QMenuBar(self)
        self.menu.addMenu('Menu')
        self.menu.setGeometry(0, 0, 640, 20)
        self.logo = QtWidgets.QLabel(self)
        self.logo.setStyleSheet('color: white')
        self.logo.setText("Dama")
        self.logo.move(250,30)
        self.logo.setFont(QFont("Proxima [Nova]", 22))


        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet('color: white')
        self.label.setText("Current Primogems")
        self.label.move(100,100)

        self.primos = self.label = QtWidgets.QLabel(self)
        self.primos.setText(self.getPrimos())
        self.primos.setStyleSheet('color: white')
        self.primos.move(100,140)

        self.b = QtWidgets.QPushButton(self)
        self.b.setText("Start")
        self.b.setStyleSheet('color: white')
        self.b.move(300,100)
        self.b.clicked.connect(self.hidebutton)
        
    
        self.term = QtWidgets.QPushButton(self)
        self.term.setStyleSheet('color: white')
        self.term.setText("Stop")
        self.term.move(300,125)
        self.term.clicked.connect(self.exit)

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setStyleSheet('color: white')
        self.stop.setText("Pause")
        self.stop.move(300,150)
        self.stop.clicked.connect( lambda: self.pauseCount(1))


        self.timer = QTimer(self)
        

    
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()




