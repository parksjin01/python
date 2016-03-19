import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import smtplib

form_class = uic.loadUiType("/usr/local/lib/python2.7/site-packages/PyQt4/mainwindow.ui")[0]

class email():
    def __init__(self, me, you, password, message):
        s=smtplib.SMTP('smtp.gmail.com')
        s.starttls()
        s.login(me, password)
        s.sendmail(me, you, message)
        s.quit()

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked)

    def btn_clicked(self):
        me = self.lineEdit.text();
        you = self.lineEdit_3.text();
        password = self.lineEdit_2.text();
        text=self.textEdit.toPlainText();
        print me, you, password, text;
        print type(me), type(you), type(password), type(text)
        me=str(me)
        you=str(you)
        password=str(password)
        text=str(text)
        print type(me), type(you), type(password), type(text)
        email(me, you, password, text);

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
