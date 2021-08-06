# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import WOM_Sensor_Kit

score = 0
WOM_Sensor_Kit.WOM_servo360(pin1, 120)
WOM_Sensor_Kit.WOM_servo360(pin2, 160)

while True:
    # If the button is pressed, start the voice-activated jumping machine
    if WOM_Sensor_Kit.WOM_button(pin8) == 1:
        display.show(Image.YES)
        sleep(500)
        # Get the current environment sound size,
        # the range of the analog value of the sound is 0-255
        soundLevel = microphone.sound_level()
        print(soundLevel)
        # Determine the lifting height by sound value
        if soundLevel < 20:
            score = 0
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 120)
            WOM_Sensor_Kit.WOM_servo360(pin2, 160)
            sleep(2000)
        if soundLevel >= 20 and soundLevel < 60:
            score = 2
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 150)
            WOM_Sensor_Kit.WOM_servo360(pin2, 130)
            sleep(2000)
        if soundLevel >= 60 and soundLevel < 100:
            score = 4
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 180)
            WOM_Sensor_Kit.WOM_servo360(pin2, 100)
            sleep(2000)
        if soundLevel >= 100 and soundLevel < 140:
            score = 6
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 210)
            WOM_Sensor_Kit.WOM_servo360(pin2, 70)
            sleep(2000)
        if soundLevel >= 140 and soundLevel < 170:
            score = 8
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 240)
            WOM_Sensor_Kit.WOM_servo360(pin2, 40)
            sleep(2000)
        if soundLevel >= 170:
            score = 10
            display.show(score)
            WOM_Sensor_Kit.WOM_servo360(pin1, 270)
            WOM_Sensor_Kit.WOM_servo360(pin2, 10)
            sleep(2000)
