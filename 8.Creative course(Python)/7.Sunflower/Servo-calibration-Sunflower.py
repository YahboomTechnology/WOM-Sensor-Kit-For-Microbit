from microbit import *
import WOM_Sensor_Kit

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    WOM_Sensor_Kit.WOM_servo360(pin10, 250)
    display.show(7)
