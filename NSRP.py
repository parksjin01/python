#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import re
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

form_class = uic.loadUiType("naver.ui")[0]

class NSRP():
    def refresh(self):
        self.response=urllib2.urlopen('http://www.naver.com')
        self.tmp=[]
        dat=self.response.read()
        r=re.search('noscript', dat)
        print r
        s=r.start()
        r=re.search('/noscript', dat)
        e=r.end()
        dat= dat[s:e + 1].split('\n')
        for i in range(4, 14):
            s=re.search('">', dat[i]).end()
            e=re.search('</', dat[i]).start()
            self.tmp.append((dat[i][s:e]))

        for i in self.tmp:
            print i
        return self.tmp


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked)
        self.NSRP=NSRP()

    def btn_clicked(self):
        self.tmp=self.NSRP.refresh()
        print self.tmp
        self.label_11.setText(unicode(self.tmp[0]))
        self.label_12.setText(unicode(self.tmp[1]))
        self.label_13.setText(unicode(self.tmp[2]))
        self.label_14.setText(unicode(self.tmp[3]))
        self.label_15.setText(unicode(self.tmp[4]))
        self.label_16.setText(unicode(self.tmp[5]))
        self.label_17.setText(unicode(self.tmp[6]))
        self.label_18.setText(unicode(self.tmp[7]))
        self.label_19.setText(unicode(self.tmp[8]))
        self.label_20.setText(unicode(self.tmp[9]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
