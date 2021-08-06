# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
WOM_Sensor_Kit.WOM_servo360(pin1, 190)
WOM_Sensor_Kit.WOM_servo360(pin2, 190)

while True:
    if WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_red) == 255:
        if (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_green) < 20) and (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_blue) < 20):
            WOM_Sensor_Kit.WOM_rgb(1023, 0, 0)
            sleep(1000)
            WOM_Sensor_Kit.WOM_rgb(0, 0, 0)
            WOM_Sensor_Kit.WOM_servo360(pin1, 220)
            WOM_Sensor_Kit.WOM_servo360(pin2, 220)
            sleep(1000)
            WOM_Sensor_Kit.WOM_servo360(pin1, 190)
            WOM_Sensor_Kit.WOM_servo360(pin2, 190)
            sleep(1000)
    elif WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_blue) == 255:
        if (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_red) < 20) and (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_green) < 20):
            WOM_Sensor_Kit.WOM_rgb(0, 0, 1023)
            sleep(1000)
            WOM_Sensor_Kit.WOM_rgb(0, 0, 0)
            WOM_Sensor_Kit.WOM_servo360(pin1, 220)
            WOM_Sensor_Kit.WOM_servo360(pin2, 150)
            sleep(1000)
            WOM_Sensor_Kit.WOM_servo360(pin1, 190)
            WOM_Sensor_Kit.WOM_servo360(pin2, 190)
            sleep(1000)
    elif WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_green) == 255:
        if (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_red) < 20) and (WOM_Sensor_Kit.WOM_color(WOM_Sensor_Kit.WOM_blue) < 20):
            WOM_Sensor_Kit.WOM_rgb(0, 1023, 0)
            sleep(1000)
            WOM_Sensor_Kit.WOM_rgb(0, 0, 0)
            WOM_Sensor_Kit.WOM_servo360(pin1, 160)
            WOM_Sensor_Kit.WOM_servo360(pin2, 150)
            sleep(1000)
            WOM_Sensor_Kit.WOM_servo360(pin1, 190)
            WOM_Sensor_Kit.WOM_servo360(pin2, 190)
            sleep(1000)