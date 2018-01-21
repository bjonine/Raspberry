# -*- coding: utf-8 -*-
# -*- code by Miaoking 2017.10.10 -*-

import wiringpi
import RPi.GPIO as GPIO
import time
import txt


# Vars
OUTPUT = 1
INPUT = 0
HIGH = 1
LOW = 0


#初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.IN)
    pass


def initWiringPi():
    wiringpi.wiringPiSetup()
    #(const int pinBase, const int numPins, const int dataPin, const int clockPin, const int latchPin) 
    wiringpi.sr595Setup(100, 32, 12, 14, 10)

def initMatrix():
    for i in range(0,32):
        wiringpi.pinMode(100 + i,OUTPUT)
    for i in range(0,8):
        wiringpi.digitalWrite(100 + i,HIGH)
        wiringpi.digitalWrite(108 + i,HIGH)
        wiringpi.digitalWrite(116 + i,HIGH)

def clearMatrix(c):
    for i in range(0,8):
        if c is 'b':
            wiringpi.digitalWrite(100 + i,HIGH)
        elif c is 'g':
            wiringpi.digitalWrite(108 + i,HIGH)
        else:
            wiringpi.digitalWrite(116 + i,HIGH)
        wiringpi.digitalWrite(124 + i,HIGH)

def drawDot(y,c,h):
    if c is 'r':
        wiringpi.digitalWrite(124 + y,h)
    elif c is 'g':
        wiringpi.digitalWrite(108 + y,h)
    elif c is 'b':
        wiringpi.digitalWrite(116 + y,h)
    elif c is 'rb':
        wiringpi.digitalWrite(124 + y,h)
        wiringpi.digitalWrite(116 + y,h)
    elif c is 'rg':
        wiringpi.digitalWrite(124 + y,h)
        wiringpi.digitalWrite(108 + y,h)
    elif c is 'bg':
        wiringpi.digitalWrite(116 + y,h)
        wiringpi.digitalWrite(108 + y,h)
    elif c is 'rbg':
        wiringpi.digitalWrite(124 + y,h)
        wiringpi.digitalWrite(116 + y,h)
        wiringpi.digitalWrite(108 + y,h)
    

def Count_down():
    for i in range(9,0,-1):
        if i is 1:
            PrintDot(txt.Zifu['1'],1,'r')
        elif i is 2:
            PrintDot(txt.Zifu['2'],1,'r')
        elif i is 3:
            PrintDot(txt.Zifu['3'],1,'r')
        elif i is 4:
            PrintDot(txt.Zifu['4'],1,'r')
        elif i is 5:
            PrintDot(txt.Zifu['5'],1,'r')
        elif i is 6:
            PrintDot(txt.Zifu['6'],1,'r')        
        elif i is 7:
            PrintDot(txt.Zifu['7'],1,'r')    
        elif i is 8:
            PrintDot(txt.Zifu['8'],1,'r')
        elif i is 9:
            PrintDot(txt.Zifu['9'],1,'r')
        elif i is 0:
            PrintDot(txt.Zifu['0'],1,'r')   

 
    
def PrintDot(Txt,t,c):
    tt = time.time()
    while True:
        for x in range(0,8):
            wiringpi.digitalWrite(100 + x,HIGH) #open
            for y in range(0,8):
                if Txt[x][y] is 1:
                    drawDot(y,c,LOW)
                drawDot(y,c,HIGH)  
            wiringpi.digitalWrite(100 + x,LOW)  #close
        if time.time() - tt > t:
             break;

def ANextZ():
    Str=[chr(i).upper() for i in range(97,123)]
    for i in Str:
        PrintDot(txt.Zifu[i],2,'r')

def Broken_LR(Txt):
    c='r'
    PrintDot(Txt,2,c)
    for num in range(0,4):
        tt = time.time()
        while True:
            for x in range(0,8):
                wiringpi.digitalWrite(100 + x,HIGH) #open
                for y in range(0,8):
                    if Txt[x][y] is 1:
                        if y>3 and y+num<8:
                            drawDot(y + num,c,LOW)
                        elif y<4 and y-num>=0:
                            drawDot(y - num,c,LOW)
                    if y>3 and y+num<8:
                        drawDot(y + num,c,HIGH)
                    elif y<4 and y-num>=0:
                        drawDot(y - num,c,HIGH)

                    
                wiringpi.digitalWrite(100 + x,LOW)  #close
            if time.time() - tt > 0.3:
                 break;
def Move_Left(Txt,t,c):
    if t>0:
        PrintDot(Txt,t,c)
        m=[0,-1,-2,-3,-4,-5,-6,-7]
    else:
        m=[7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7]
    for num in m:
        tt = time.time()
        while True:
            for x in range(0,8):
                wiringpi.digitalWrite(100 + x,HIGH) #open
                for y in range(0,8):
                    if Txt[x][y] is 1:
                        if y+num>=0:drawDot(y + num,c,LOW) #no in shuang zhi bianse xunhuan
                    if y+num>=0:drawDot(y + num,c,HIGH)  
                wiringpi.digitalWrite(100 + x,LOW)  #close
            if time.time() - tt > 0.3:
                 break;
                
def Move_Up(Txt,t,c):
    if t>0:
        PrintDot(Txt,t,c)
        m=[0,1,2,3,4,5,6,7]
    else:
        m=[-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
    for num in m:
        tt = time.time()
        while True:
            for x in range(0,8):
                wiringpi.digitalWrite(100 + x,HIGH) #open
                for y in range(0,8):
                    if x+num <8 and x+num>0:
                        e=x+num                                           
                        if Txt[e][y] is 1:
                            drawDot(y,c,LOW)                     
                        drawDot(y,c,HIGH)
                    
                wiringpi.digitalWrite(100 + x,LOW)  #close
            if time.time() - tt > 0.3:
                 break;

def Move_Down(Txt,t,c):
    if t>0:
        PrintDot(Txt,t,c)
        m=[0,-1,-2,-3,-4,-5,-6,-7]
    else:
        m=[7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7]
    for num in m:
        tt = time.time()
        while True:
            for x in range(0,8):
                wiringpi.digitalWrite(100 + x,HIGH) #open
                for y in range(0,8):
                    if x+num <8 and x+num>0:
                        e=x+num                                           
                        if Txt[e][y] is 1:
                            drawDot(y,c,LOW)                     
                        drawDot(y,c,HIGH)
                    
                wiringpi.digitalWrite(100 + x,LOW)  #close
            if time.time() - tt > 0.3:
                 break;


def RemoveTwo(j):
    l=[]
    jnum=0
    for y in range(len(j[0])):
        n=0
        for x in range(0,8):
            n += j[x][y]
        if n is 0:
            jnum += 1
        else:
            jnum = 0

        if jnum>1: #这里设相邻的两个字符空几列
            l.append(y)
            
    for x in range(0,8):
        i=0
        for y in l:
            j[x].pop(y-i)
            i += 1
    return;
            


def Move_Txt(Text,c):
    j = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
    
    for i in list(Text):
        if i in txt.Zifu.keys():
            for x in range(0,8):
                j[x].extend(txt.Zifu[i][x])
    
    RemoveTwo(j)

    
    for num in range(0,len(j[0])):
        tt = time.time()
        while True:
            for x in range(0,8):
                wiringpi.digitalWrite(100 + x,HIGH) #open
                for y in range(num,num+8):
                    if y<len(j[x]):
                        if j[x][y] is 1:
                            if y-num>=0:drawDot(y - num ,c,LOW) #no in shuang zhi bianse xunhuan
                        if y-num>=0:drawDot(y - num,c,HIGH)  
                wiringpi.digitalWrite(100 + x,LOW)  #close
            if time.time() - tt > 0.3:
                 break;
    
def detct():
    import random
    while True:
        #如果感应器针脚输出为True，则打印信息并执行蜂鸣器函数
        #PrintDot(txt.Zifu['?'],1,'r')
        if GPIO.input(7) == False:            
            #print (GPIO.input(7))
        #else:
            l = random.randint(1,6)
            print (0)
            Move_Up(txt.Zifu['Face_'+str(l)],5,'rb')            
            #break;

                
# kaishi 
initWiringPi()
initMatrix()
clearMatrix('b')
init()
      
PrintDot(txt.Zifu['smile'],2,'rb')

detct()
         
