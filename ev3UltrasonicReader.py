#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.button import Button
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)
log.info("Starting Ultrasonic Reader Program")


button = Button()
us = UltrasonicSensor()

try:
    while not button.any():
        #us.mode = 'MODE_US_DIST_IN'
        distance = str( us.distance_centimeters_continuous)
        log.info('Distance in centimeters ' + distance)
        sleep(.5)

except(GracefulShutdown, Exception) as e:
    log.exception(e)

log.info('Exiting Ultrasonic Sensor Reader Program')


