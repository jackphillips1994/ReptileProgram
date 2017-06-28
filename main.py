# Main program

import time

# Importing custom modules
import Sensors
from Adafruit_CharLCD import Adafruit_CharLCD

# Setup the GPIO pins
GPIO_list = {'manual_button': 3, 'relay_1': 14, 'relay_2': 15, 'relay_3': 18,
             'relay_4': 2,'relay_5': 23}
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_list[manual_button],GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Setting up the GPIO pins for the LCD Display
lcd = Adafruit_CharLCD(rs=26,en=19,d4=13,d5=6,d6=5,d7=11,cols=16,lines=2)

def create_sensors(name):
    name = sensors.Sensors()

def read_temperature():


def main():
