# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()

while True:
    if WOM_Sensor_Kit.WOM_light(pin0) > 800:
        WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)
    if WOM_Sensor_Kit.WOM_light(pin0) < 800:
        WOM_Sensor_Kit.WOM_rgb(0, 0, 0)