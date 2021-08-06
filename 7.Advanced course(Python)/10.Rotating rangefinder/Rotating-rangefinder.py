# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 180
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_ultrasonic(pin7, pin6))
    WOM_Sensor_Kit.WOM_servo360(pin1, x)
    sleep(100)
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_up):
        x = x - 10
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_down):
        x = x + 10
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_left):
        x = x + 10
    if WOM_Sensor_Kit.WOM_rocker(pin3, pin4, WOM_Sensor_Kit.WOM_right):
        x = x - 10
    if x < 1:
        x = 1
    if x > 360:
        x = 360