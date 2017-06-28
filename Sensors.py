# Python file that contains the sensor class
# More than temperature sensors can be added to this program

import time

# Dictionary that contains the device and device IDs of each
# of the sensors
class Sensor:
    def __init__(self, name, sensor_type):
        self.__sensor_name = name
        self.__sensor_type = sensor_type
        self.__reading_incrementation = 2.0

    # Functions that handle setting the attributes
    def set_name(self, name):
        self.__sensor_name = name

    def set_type(self, sensor_type):
        self.__sensor_type = sensor_type

    def set_sensor_device_ID(self, device_ID):
        self.__sensor_device_ID = device_ID

    def __set_reading_incrementation(name, value):
        self.__reading_incrementation = value

    # Functions that handle returning the attributes
    def get_name(self):
        return self.__sensor_name

    def get_type(self):
        return self.__sensor_type

    def get_reading_incrementation(self):
        return self.__reading_incrementation
