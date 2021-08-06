# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    WOM_Sensor_Kit.WOM_display(
       WOM_Sensor_Kit.WOM_dht11(pin0, WOM_Sensor_Kit.WOM_temp_C))
    sleep(1500)
