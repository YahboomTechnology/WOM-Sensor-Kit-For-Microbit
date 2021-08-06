# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music
import WOM_Sensor_Kit

display.off()
WOM_Sensor_Kit.WOM_servo360(pin1, 190)
WOM_Sensor_Kit.WOM_servo360(pin2, 190)

while True:
    print(WOM_Sensor_Kit.WOM_pir(pin0))

    if WOM_Sensor_Kit.WOM_pir(pin0) == 1:
        # Open the door
        WOM_Sensor_Kit.WOM_servo360(pin2, 80)
        sleep(100)
        WOM_Sensor_Kit.WOM_servo360(pin1, 290)
        sleep(100)
        WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)
        music.play(music.POWER_UP)
        sleep(2000)
        # Close the door
        WOM_Sensor_Kit.WOM_servo360(pin2, 190)
        sleep(100)
        WOM_Sensor_Kit.WOM_servo360(pin1, 190)
        sleep(100)
        WOM_Sensor_Kit.WOM_rgb(0, 0, 0)
        music.play(music.POWER_DOWN)
        sleep(100)