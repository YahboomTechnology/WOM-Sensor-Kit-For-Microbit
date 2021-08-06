# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

while True:
    # Parameter definition: WOM_ultrasonic(Echo,Trig)
    display.scroll(WOM_Sensor_Kit.WOM_ultrasonic(pin1, pin0))
    sleep(100)