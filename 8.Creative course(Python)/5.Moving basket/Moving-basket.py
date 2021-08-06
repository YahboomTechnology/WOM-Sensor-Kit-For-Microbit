# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit
import music

display.off()
x = 0
y = 0
num = 0
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    WOM_Sensor_Kit.WOM_display(num)
    if WOM_Sensor_Kit.WOM_ir(pin2) == 0:
        num = num + 1
        WOM_Sensor_Kit.WOM_display(num)
        music.play(music.BA_DING)
        sleep(20)

    if WOM_Sensor_Kit.WOM_button(pin3) == 1:
        while True:
            for x in range(0, 70):
                y = x + 150
                WOM_Sensor_Kit.WOM_servo360(pin1, y)
                if WOM_Sensor_Kit.WOM_ir(pin2) == 0:
                    num = num + 1
                    WOM_Sensor_Kit.WOM_display(num)
                    music.play(music.BA_DING)
                    sleep(20)
                sleep(10)
            for x in range(0, 75):
                y = 220 - x
                WOM_Sensor_Kit.WOM_servo360(pin1, y)
                if WOM_Sensor_Kit.WOM_ir(pin2) == 0:
                    num = num + 1
                    WOM_Sensor_Kit.WOM_display(num)
                    music.play(music.BA_DING)
                    sleep(20)
                sleep(10)


