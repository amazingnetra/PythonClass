#!/usr/bin/env python3

from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG, 
                format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)
log.info("Starting Reflected Light Reader program")

btn = Button()
tankMove = MoveTank(OUTPUT_A, OUTPUT_D)
cs = ColorSensor()
d = Display()

try:

    while not btn.any():
        intensity = cs.reflected_light_intensity
        strIntensity = str(intensity)
        log.info(strIntensity)
        sleep(0.5)

except (GracefulShutdown, Exception) as e:
    log.exception(e)

log.info('Exiting Reflected Light Reader Program')