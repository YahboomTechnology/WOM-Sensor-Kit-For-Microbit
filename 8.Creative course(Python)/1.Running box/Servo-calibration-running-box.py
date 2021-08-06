from microbit import *
import WOM_Sensor_Kit

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    WOM_Sensor_Kit.WOM_servo360(pin2, 180)
    display.show(1)
