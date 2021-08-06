# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 180
y = 140

while True:
    WOM_Sensor_Kit.WOM_servo360(pin2, y)
    WOM_Sensor_Kit.WOM_servo360(pin1, x)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_up):
        y = y + 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_down):
        y = y - 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_left):
        x = x - 1
        sleep(10)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_right):
        x = x + 1
        sleep(10)
    if x < 150:
        x = 150
    if x > 220:
        x = 220
    if y < 70:
        y = 70
    if y > 160:
        y = 150