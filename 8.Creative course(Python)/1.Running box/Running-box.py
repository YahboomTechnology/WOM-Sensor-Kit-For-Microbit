from microbit import *
import WOM_Sensor_Kit

people_1 = Image("00900:09990:90909:09090:09090")
people_2 = Image("00900:09990:90909:09090:90009")

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, 180)
    WOM_Sensor_Kit.WOM_servo360(pin2, 180)
    if WOM_Sensor_Kit.WOM_pir(pin0) == 1:
        display.show(people_1)
        WOM_Sensor_Kit.WOM_servo360(pin1, 130)
        WOM_Sensor_Kit.WOM_servo360(pin2, 130)
        sleep(500)
        display.show(people_2)
        WOM_Sensor_Kit.WOM_servo360(pin1, 220)
        WOM_Sensor_Kit.WOM_servo360(pin2, 220)
        sleep(500)
        display.show(people_1)
        WOM_Sensor_Kit.WOM_servo360(pin1, 130)
        WOM_Sensor_Kit.WOM_servo360(pin2, 130)
        sleep(500)
        display.show(people_2)
        WOM_Sensor_Kit.WOM_servo360(pin1, 220)
        WOM_Sensor_Kit.WOM_servo360(pin2, 220)
        sleep(500)
    if WOM_Sensor_Kit.WOM_pir(pin0) == 0:
        display.show(Image.YES)