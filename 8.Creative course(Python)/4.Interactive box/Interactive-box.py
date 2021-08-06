# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit
import random

boring = Image("00000:99099:00000:00000:09990")
angry = Image("90009:09090:00000:09990:90009")

while True:
    display.show(boring)
    WOM_Sensor_Kit.WOM_servo360(pin1, 170)
    if WOM_Sensor_Kit.WOM_pir(pin2) == 0:
        display.show(angry)
        num = random.randint(0, 4)
        if num == 3:
            for num in range(0, 2):
                WOM_Sensor_Kit.WOM_servo360(pin1, 290)
                sleep(300)
                WOM_Sensor_Kit.WOM_servo360(pin1, 170)
                sleep(200)
        WOM_Sensor_Kit.WOM_servo360(pin1, 290)
        sleep(300)
        WOM_Sensor_Kit.WOM_servo360(pin1, 170)
        sleep(200)