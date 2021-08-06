# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 200
y = 250
WOM_Sensor_Kit.WOM_init_display(7)
value = [0, 0, 0, 0, 0, 0]
minimum = 1023

while True:
    WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
    WOM_Sensor_Kit.WOM_servo360(pin1, 200)
    WOM_Sensor_Kit.WOM_servo360(pin10, 250)

    if WOM_Sensor_Kit.WOM_button(pin0) == 1:
        WOM_Sensor_Kit.WOM_servo360(pin1, 200)
        WOM_Sensor_Kit.WOM_servo360(pin10, 300)
        sleep(500)
        value[0] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[0])
        WOM_Sensor_Kit.WOM_servo360(pin1, 250)
        WOM_Sensor_Kit.WOM_servo360(pin10, 300)
        sleep(500)
        value[1] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[1])
        WOM_Sensor_Kit.WOM_servo360(pin1, 250)
        WOM_Sensor_Kit.WOM_servo360(pin10, 240)
        sleep(500)
        value[2] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[2])
        WOM_Sensor_Kit.WOM_servo360(pin1, 200)
        WOM_Sensor_Kit.WOM_servo360(pin10, 240)
        sleep(500)
        value[3] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[3])
        WOM_Sensor_Kit.WOM_servo360(pin1, 130)
        WOM_Sensor_Kit.WOM_servo360(pin10, 240)
        sleep(500)
        value[4] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[4])
        WOM_Sensor_Kit.WOM_servo360(pin1, 130)
        WOM_Sensor_Kit.WOM_servo360(pin10, 300)
        sleep(500)
        value[5] = WOM_Sensor_Kit.WOM_light(pin2)
        WOM_Sensor_Kit.WOM_display(WOM_Sensor_Kit.WOM_light(pin2))
        print(value[5])
        WOM_Sensor_Kit.WOM_servo360(pin1, 200)
        WOM_Sensor_Kit.WOM_servo360(pin10, 300)
        sleep(500)
        for i in range(6):
            if value[i] < minimum:
                minimum = value[i]
                print(minimum)
        if value[0] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 200)
            WOM_Sensor_Kit.WOM_servo360(pin10, 300)
            sleep(5000)
        if value[1] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 250)
            WOM_Sensor_Kit.WOM_servo360(pin10, 300)
            sleep(5000)
        if value[2] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 250)
            WOM_Sensor_Kit.WOM_servo360(pin10, 240)
            sleep(5000)
        if value[3] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 200)
            WOM_Sensor_Kit.WOM_servo360(pin10, 240)
            sleep(5000)
        if value[4] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            WOM_Sensor_Kit.WOM_servo360(pin10, 240)
            sleep(5000)
        if value[5] == minimum:
            WOM_Sensor_Kit.WOM_servo360(pin1, 130)
            WOM_Sensor_Kit.WOM_servo360(pin10, 300)
            sleep(5000)
        minimum = 1023
