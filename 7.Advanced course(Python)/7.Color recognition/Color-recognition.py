# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
r = 0
g = 0
b = 0

while True:
    r = WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_red) * 4
    g = WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_green) * 4
    b = WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_blue) * 4
    WOM_Sensor_Kit.WOM_rgb(r, g, b)