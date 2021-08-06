# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 230

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, x)
    if WOM_Sensor_Kit.WOM_rocker(pin2, pin3, WOM_Sensor_Kit.WOM_up):
        x = x - 4
    if WOM_Sensor_Kit.WOM_rocker(pin2, pin3, WOM_Sensor_Kit.WOM_down):
        x = x + 4
    if WOM_Sensor_Kit.WOM_rocker(pin2, pin3, WOM_Sensor_Kit.WOM_left):
        x = x - 4
    if WOM_Sensor_Kit.WOM_rocker(pin2, pin3, WOM_Sensor_Kit.WOM_right):
        x = x + 4
    if x < 130:
        x = 130
    if x > 230:
        x = 230
    if WOM_Sensor_Kit.WOM_button(pin0) == 1:
        sleep(500)
        if WOM_Sensor_Kit.WOM_button(pin0) == 1:
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            sleep(500)
            WOM_Sensor_Kit.WOM_servo360(pin1, 230)
            sleep(500)
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            sleep(500)
            WOM_Sensor_Kit.WOM_servo360(pin1, 230)
            sleep(500)
        else:
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            sleep(300)
            WOM_Sensor_Kit.WOM_servo360(pin1, 230)
            sleep(300)
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            sleep(300)
            WOM_Sensor_Kit.WOM_servo360(pin1, 230)
            sleep(300)