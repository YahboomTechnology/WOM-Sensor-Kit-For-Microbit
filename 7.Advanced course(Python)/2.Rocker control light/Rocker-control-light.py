# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()

while True:
    if WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_up):
        WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_down):
        WOM_Sensor_Kit.WOM_rgb(0, 0, 1023)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_left):
        WOM_Sensor_Kit.WOM_rgb(1023, 0, 0)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_right):
        WOM_Sensor_Kit.WOM_rgb(0, 1023, 0)