# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music
import WOM_Sensor_Kit

people_1 = Image("00900:09990:90909:09090:09090")

while True:
    if WOM_Sensor_Kit.WOM_pir(pin0) == 1:
        display.show(people_1)
        music.play(music.CHASE)
    if WOM_Sensor_Kit.WOM_pir(pin0) == 0:
        display.show(Image.YES)