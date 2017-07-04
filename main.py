# Main program

import time
import datetime

# Importing custom modules
from model import SensorData
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

# Setup the GPIO pins
GPIO_list = {'button': 3, 'relay_1': 14, 'relay_2': 15, 'relay_3': 18,
             'relay_4': 2,'relay_5': 23}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_list['button'],GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Setting up the GPIO pins for the LCD Display
lcd = Adafruit_CharLCD(rs=26,en=19,d4=13,d5=6,d6=5,d7=11,cols=16,lines=2)

# Sensor list with the device ID of each of the temperature sensors
DS18B20_sensor_ID_List = {'sensor_one': '28-0516929ddeff', 'sensor_two': '28-0516a43fb9ff',
                  'sensor_three': '28-0416a42716ff', 'sensor_four': '28-0516a4a711ff',
                  'sensor_five': '28-0316a27de9ff'}

# Due to some temperature sensors needing to be read as a file a seperate
# function was created to read these files
def read_in_line_sensor(sensor):
    reading_time = datetime.datetime.now()
    temp_store = open("/sys/bus/w1/devices/{0}/w1_slave".format(sensor.device_id))
    temp = temp_store.read()
    temp_store.close()
    temp_data = temp.split("\n")[1].split(" ")[9]
    temperature = float(temp_data[2:])
    temperature = temperature / 1000
    return sensor.name, temperature, reading_time

# Function created to read sensors that just input data through to a GPIO
#def read_GPIO_sensor():

# Function to read and display the temperature on the LCD screen
def LCD_display(sensor, temperature):
    lcd.clear()
    lcd.message('{0}\nTemp: {1}'.format(sensor,temperature))


# Function to handle cycling through the sensors when the button is pressed
def button_pressed(button):
    input_state = GPIO.input(button)
    if input_state == False:
        print("Button Pressed")
        return True
