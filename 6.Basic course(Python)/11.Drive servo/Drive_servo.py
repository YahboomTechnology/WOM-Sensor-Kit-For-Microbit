# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()

while True:
    # Parameter definition: WOM_servo360 (pin, angle)
    WOM_Sensor_Kit.WOM_servo360(pin1, 0)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 90)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 270)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 360)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 270)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 90)
    sleep(1000)
    WOM_Sensor_Kit.WOM_servo360(pin1, 0)