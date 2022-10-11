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
        ip2='可以通ping的内网ip地址:  '+ip1
        text3.append(ip2)

        file = open('data/data1.txt','a')
        file.write(ip1 + '\n')
        file.close()

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

    file = open('data/data1.txt','w')
    file.write('')
    file.close()

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

button1 = QPushButton('开始高速扫描(配置低会崩溃)', window)
button1.move(160,15)
button1.resize(220,30)
button1.clicked.connect(thread0)

window2 = QMainWindow()
window2.resize(580, 720)
window2.move(550, 150)
window2.setWindowTitle('IntranetAnalysis -ip历史列表')

text4 = QTextBrowser(window2)
text4.move(30,15)
text4.resize(540,650)

window3 = QMainWindow()
window3.resize(600, 750)
window3.move(550, 100)
window3.setWindowTitle('IntranetAnalysis -ip分析')

text5 = QTextBrowser(window3)
text5.move(30,15)
text5.resize(540,720)

def opWindow3():
    ''''''
    window3.show()

def opWindow2():
    ''''''
    window2.show()
    file = open('data/data1.txt','r')
    text4read = file.read()
    text4.setText(text4read)
    text4.append('以上ip地址为历史记录，点击开始分析以分析以上ip地址')

def opWindow21():
    ''''''
    window2.close()
    opWindow3()

button2 = QPushButton('直接开始分析', window)
button2.move(450,15)
button2.resize(120,30)
button2.clicked.connect(opWindow2)

button3 = QPushButton('开始分析', window2)
button3.move(450,680)
button3.resize(120,30)
button3.clicked.connect(opWindow21)

window.show()
app.exec_()
