# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

display.off()
x = 0
y = 0
ago = 0
now = 0

while True:
    ago = WOM_Sensor_Kit.WOM_ultrasonic(pin3, pin2)
    sleep(20)
    now = WOM_Sensor_Kit.WOM_ultrasonic(pin3, pin2)
    sleep(20)
    print('ago:')
    print(ago)
    print('now:')
    print(ago)
    if now > 2 and ago > 2:
        if (now - ago < 10 and now - ago > 0) or (ago - now < 10 and ago - now > 0):
            if WOM_Sensor_Kit.WOM_ultrasonic(pin3, pin2) > 20 and WOM_Sensor_Kit.WOM_ultrasonic(pin3, pin2) < 30:
                for x in range(0, 50):
                    y = x + 130
                    WOM_Sensor_Kit.WOM_servo360(pin1, y)
                    sleep(15)
                for x in range(0, 50):
                    y = 180 - x
                    WOM_Sensor_Kit.WOM_servo360(pin1, y)
                    sleep(15)
            if WOM_Sensor_Kit.WOM_ultrasonic(pin3, pin2) < 20:
                for x in range(0, 50):
                    y = x + 130
                    WOM_Sensor_Kit.WOM_servo360(pin1, y)
                    sleep(5)
                for x in range(0, 50):
                    y = 180 - x
                    WOM_Sensor_Kit.WOM_servo360(pin1, y)
                    sleep(5)


