# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_pir (pin) someone returns 1
    if (WOM_Sensor_Kit.WOM_pir(pin0)) == 1:
        display.show(1)
    else:
        display.show(0)