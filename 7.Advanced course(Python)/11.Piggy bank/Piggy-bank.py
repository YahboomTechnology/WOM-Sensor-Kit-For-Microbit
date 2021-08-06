# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music
import WOM_Sensor_Kit

display.off()
score = 0
WOM_Sensor_Kit.WOM_init_display(7)

while True:
    WOM_Sensor_Kit.WOM_display(score)
    if (WOM_Sensor_Kit.WOM_ir(pin2)) == 0:
        score = score + 1
        WOM_Sensor_Kit.WOM_display(score)
        music.play(music.BA_DING)
    sleep(100)