# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music
import WOM_Sensor_Kit

display.off()

while True:
    if (WOM_Sensor_Kit.WOM_ir(pin0)) == 0:
        music.play(music.DADADADUM)