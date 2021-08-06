# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_ir (pin), return 0 if there is an obstacle,
    # return 1 if there is no obstacle
    if (WOM_Sensor_Kit.WOM_ir(pin0)) == 0:
        display.show(1)
    else:
        display.show(0)