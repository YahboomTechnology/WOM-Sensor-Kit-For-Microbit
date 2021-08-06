from microbit import *
import WOM_Sensor_Kit

people_1 = Image("00900:09990:90909:09090:09090")
people_2 = Image("00900:09990:90909:09090:90009")

while True:
    if WOM_Sensor_Kit.WOM_pir(pin0) == 1:
        display.show(people_1)
        sleep(100)
        display.show(people_2)
        sleep(100)
        display.show(people_1)
        sleep(100)
        display.show(people_2)
        sleep(100)
    if WOM_Sensor_Kit.WOM_pir(pin0) == 0:
        display.show(Image.YES)