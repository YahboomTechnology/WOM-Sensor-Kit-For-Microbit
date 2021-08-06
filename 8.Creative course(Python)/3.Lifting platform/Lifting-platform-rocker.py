# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 120
y = 160

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, x)
    WOM_Sensor_Kit.WOM_servo360(pin2, y)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_up):
        x = x - 4
        y = y + 4
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_down):
        x = x + 4
        y = y - 4
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_left):
        x = x - 4
        y = y + 4
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_right):
        x = x + 4
        y = y - 4
    if x < 120:
        x = 120
    if x > 270:
        x = 270
    if y < 10:
        y = 10
    if y > 160:
        y = 160
    print(x)
    print(y)

