# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_color (obtained color)
    display.scroll('R:')
    display.scroll(WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_red))
    sleep(1000)
    display.scroll('G:')
    display.scroll(WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_green))
    sleep(1000)
    display.scroll('B:')
    display.scroll(WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_blue))
    sleep(1000)