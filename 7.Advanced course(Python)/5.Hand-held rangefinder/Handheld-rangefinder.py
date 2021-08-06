# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_ultrasonic(pin1, pin0))
    sleep(100)