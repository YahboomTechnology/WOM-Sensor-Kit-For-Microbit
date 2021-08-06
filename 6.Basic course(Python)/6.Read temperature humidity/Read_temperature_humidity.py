# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_dht11 (pin, read data)
    # Return corresponding data, including WOM_temp_C, WOM_temp_F, WOM_humidity
    # The interval of each acquisition must be more than 1s
    display.show("C ")
    display.scroll(WOM_Sensor_Kit.WOM_dht11(pin0, WOM_Sensor_Kit.WOM_temp_C))
    sleep(1500)
    display.show("F ")
    display.scroll(WOM_Sensor_Kit.WOM_dht11(pin0, WOM_Sensor_Kit.WOM_temp_F))
    sleep(1500)
    display.show("H ")
    display.scroll(WOM_Sensor_Kit.WOM_dht11(pin0, WOM_Sensor_Kit.WOM_humidity))
    sleep(1500)