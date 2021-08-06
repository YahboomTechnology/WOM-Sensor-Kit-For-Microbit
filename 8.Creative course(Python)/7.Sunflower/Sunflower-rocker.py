# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 190
y = 250
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    #数码管显示光敏的模拟值，模拟量范围0-1023，光照越强，数值越小。
    #通过摇杆控制二自由度向日葵上下左右运动。
    WOM_Sensor_Kit.WOM_servo360(pin1,x)
    WOM_Sensor_Kit.WOM_servo360(pin10,y)
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin0))
    if WOM_Sensor_Kit.WOM_rocker(pin3,pin4,WOM_Sensor_Kit.WOM_up):
        y = y + 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3,pin4,WOM_Sensor_Kit.WOM_down):
        y = y - 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3,pin4,WOM_Sensor_Kit.WOM_left):
        x = x + 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3,pin4,WOM_Sensor_Kit.WOM_right):
        x = x - 1
        sleep(10)
    #舵机P1活动范围限定在60-300之间，舵机P10的活动范围限定在190-280之间
    if x < 60:
        x = 60
    if x > 300:
        x = 300
    if y < 190:
        y = 190
    if y > 280:
        y = 280
