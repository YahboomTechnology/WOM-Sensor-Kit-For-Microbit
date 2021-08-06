# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

WOM_Sensor_Kit.WOM_init_display(7)

while True:
    # Parameter definition: WOM_dht11 (pin, read data)
    # Return corresponding data, including WOM_temp_C, WOM_temp_F, WOM_humidity
    display.show("H")
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_dht11(
       pin0, WOM_Sensor_Kit.WOM_humidity))
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    # Time interval must be more than 1s
    sleep(2000)
    display.show("T")
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_dht11(
       pin0, WOM_Sensor_Kit.WOM_temp_C))
    WOM_Sensor_Kit.WOM_servo360(pin1, 95)
    # Time interval must be more than 1s
    sleep(2000)