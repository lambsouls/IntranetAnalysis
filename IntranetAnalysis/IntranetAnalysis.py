import itertools
import os
import time
import random
import urllib.request
import requests
import re
import random
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit , QTextBrowser , QLineEdit
from threading import Thread
from time import sleep
from multiping import MultiPing

def hanshu1(a1,a2):
    ''''''
    ip1 = '192.168.'+str(a1)+'.'+str(a2)
    mp = MultiPing([ip1])
    mp.send()
    responses, no_responses = mp.receive(1)
    if no_responses==[]:
        print(ip1)
        sleep(random.randint(30,60))
        ip1='可以通ping的内网ip地址:  '+ip1
        text3.append(ip1)
    #print(no_responses)
    return(no_responses)

def thread2(time1):
    ''''''
    if time1=='0':
        time2=0
    if time1=='1':
        time2=0.003
    a1=0
    a2=0
    ax=0
    while ax == 0:
        ip1 = '192.168.'+str(a1)+'.'+str(a2)
        text2.setText('正在ping内外ip地址:  ' + ip1)
        #print(ip1)
        try:
            thread = Thread(
                target=hanshu1, 
                args=(a1,a2)
            )

            thread.start()
            sleep(time2)
        except:
            print('error')

        if a1 == 255:
            if a2 == 255:
                ax=1
                text2.setText('收尾中。。。')
                sleep(60)
                text2.setText('内网IP地址扫描完毕。')
            elif a2 != 255:
                a2+=1
        elif a1 != 255:
            if a2 == 255:
                a1+=1
                a2=0
            elif a2 != 255:
                a2+=1

def thread1():
    ''''''
    thread = Thread(
            target=thread2, 
            args=('1')
        )

    thread.start()

def thread0():
    ''''''
    thread = Thread(
            target=thread2, 
            args=('0')
        )

    thread.start()

app = QApplication([])

window = QMainWindow()
window.resize(600, 750)
window.move(500, 50)
window.setWindowTitle('IntranetAnalysis')

text2 = QLineEdit(window)
text2.move(30,50)
text2.resize(540,30)

text3 = QTextBrowser(window)
text3.move(30,85)
text3.resize(540,650)

button0 = QPushButton('开始普通扫描', window)
button0.move(30,15)
button0.resize(120,30)
button0.clicked.connect(thread1)

button0 = QPushButton('开始高速扫描(配置低会崩溃)', window)
button0.move(160,15)
button0.resize(220,30)
button0.clicked.connect(thread0)

window.show()
app.exec_()
