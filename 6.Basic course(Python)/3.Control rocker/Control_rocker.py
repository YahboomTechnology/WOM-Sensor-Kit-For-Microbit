# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_rocker (pin X, pin Y, status) returns 1 or 0
    if WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_up) == 1:
        display.show(Image.ARROW_N)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_down) == 1:
        display.show(Image.ARROW_S)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_left) == 1:
        display.show(Image.ARROW_E)
    elif WOM_Sensor_Kit.WOM_rocker(pin0, pin1, WOM_Sensor_Kit.WOM_right) == 1:
        display.show(Image.ARROW_W)