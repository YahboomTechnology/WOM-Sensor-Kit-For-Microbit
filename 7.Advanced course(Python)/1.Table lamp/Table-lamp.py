# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
temp = 0
WOM_Sensor_Kit.WOM_rgb(0, 0, 0)

while True:
    if WOM_Sensor_Kit.WOM_button(pin0) == 1:
        sleep(300)
        temp = temp + 1
        sleep(200)
        if temp == 2:
            temp = 0
        if temp == 0:
            WOM_Sensor_Kit.WOM_rgb(0, 0, 0)
        if temp == 1:
            WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)