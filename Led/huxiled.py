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

    # 创建一个 PWM 实例，需要两个参数，第一个是GPIO端口号
    # 第二个是频率（Hz），频率越高LED看上去越不会闪烁，相应对CPU要求就越高，设置合适的值就可以
    pwm = GPIO.PWM(PIN_NO, 50) # 通道为 37 ,频率越小闪烁越厉害

    # 启用 PWM，参数是占空比，范围：0.0 <= 占空比 >= 100.0
    pwm.start(0)
    try:
        while True:
            # 电流从小到大，LED由暗到亮
            for i in range(0, 101,2):
                pwm.ChangeDutyCycle(i) # 更改占空比范围：0.0 <= dc >= 100.0
                print(i)
                time.sleep(.1)
            # 再让电流从大到小，LED由亮变暗
            for i in range(100,-1,-2):
                pwm.ChangeDutyCycle(i)
                time.sleep(.1)
                print('--',i)

    except KeyboardInterrupt:
        pass

    # 停用 PWM
    pwm.stop()

    # 清理GPIO口
    RPi.GPIO.cleanup()

# 最后一段是一个小技巧。这个程序如果不强制停止会不停地执行下去。
# 而Ctrl+C强制终端程序的话，GPIO口又没有机会清理。
# 加上一个try except 可以捕捉到Ctrl+C强制中断的动作，
# 试图强制中断时，程序不会马上停止而是会先跳到这里来做一些你想做完的事情，比如清理GPIO口。
