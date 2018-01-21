import RPi.GPIO as GPIO
import time

PIN_NO = 37 # 蜂鸣器GPIO编号

#初始化
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_NO,GPIO.OUT) #OUT输出

def map(x, in_min, in_max, out_min, out_max):   # 将一个数从一个区间线性映射到另一个区间，比如将0~100之间的一个数映射到0~255之间
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ =='__main__':
    init()
    GPIO.output(PIN_NO, GPIO.HIGH)
    time.sleep(12)
    GPIO.output(PIN_NO, GPIO.LOW)


