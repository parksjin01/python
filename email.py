import smtplib
from Tkinter import *
import tkSimpleDialog

class email():
    def __init__(self, me, you, password, message):
        s=smtplib.SMTP('smtp.gmail.com')
        s.starttls()
        s.login(me, password)
        s.sendmail(me, you, message)
        s.quit()

class Send():
    def __init__(self, master):
        me=tkSimpleDialog.askstring(master,'Type you email')
        you=tkSimpleDialog.askstring(master, 'Type counterparts email')
        password=tkSimpleDialog.askstring(master, 'Type password')
        message=tkSimpleDialog.askstring(master, 'Type message')
        try:
            email(me, you, password, message)
            l=Label(master, text='I send email successful')
        except:
            l=Label(master, text='Error is occured')
        finally:
            l.pack()


root=Tk()
Send(root)
root.mainloop()
