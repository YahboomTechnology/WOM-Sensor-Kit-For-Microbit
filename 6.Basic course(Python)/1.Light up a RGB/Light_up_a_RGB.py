# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()

while True:
    # Parameter definition: WOM_rgb (red, green, blue) color range: 0-1023
    WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)
    sleep(100)