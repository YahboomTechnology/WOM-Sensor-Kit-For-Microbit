# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit
num = 0

while True:
    # Parameter definition: WOM_light (pin) returns the analog value 0-1023
    num = 1023 - WOM_Sensor_Kit.WOM_light(pin0)
    display.scroll(num)
    sleep(100)