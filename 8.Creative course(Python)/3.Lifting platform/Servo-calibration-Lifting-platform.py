from microbit import *
import WOM_Sensor_Kit

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, 130)
    WOM_Sensor_Kit.WOM_servo360(pin2, 130)
    display.show(3)
