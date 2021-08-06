# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
# Parameter definition: WOM_init_display (brightness level) range 0-7,
# 0 is the largest, 1 is the smallest, and 1-7 is incremented
WOM_Sensor_Kit.WOM_init_display(7)
while True:
    # Parameter definition: WOM_display (number) display number range 0-9999
    WOM_Sensor_Kit.WOM_display(1234)
    sleep(100)