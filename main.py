# Main program

import time
import datetime

# Importing custom modules
from model import SensorData
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

# Setup the GPIO pins
GPIO_list = {'manual_button': 3, 'relay_1': 14, 'relay_2': 15, 'relay_3': 18,
             'relay_4': 2,'relay_5': 23}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_list['manual_button'],GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Setting up the GPIO pins for the LCD Display
lcd = Adafruit_CharLCD(rs=26,en=19,d4=13,d5=6,d6=5,d7=11,cols=16,lines=2)

# Sensor list with the device ID of each of the temperature sensors
DS18B20_sensor_ID_List = {'sensor_one': '28-0516929ddeff', 'sensor_two': '28-0516a43fb9ff',
                  'sensor_three': '28-0416a42716ff', 'sensor_four': 'blank',
                  'sensor_five': 'blank'}

# Due to some temperature sensors needing to be read as a file a seperate
# function was created to read these files
def read_in_line_sensor(data):
    while True:
        reading_time = datetime.datetime.now()
        for sensor in data.get_sensors():
            temp_store = open("/sys/bus/w1/devices/{0}/w1_slave".format(sensor.device_id))
            temp = temp_store.read()
            temp_store.close()
            temp_data = temp.split("\n")[1].split(" ")[9]
            temperature = float(temp_data[2:])
            temperature = temperature / 1000
            print("Sensor {0} current reading is: {1}".format(sensor.name, temperature))
        time.sleep(2.0)

# Function created to read sensors that just input data through to a GPIO
#def read_GPIO_sensor():

def main():
    data = SensorData()

    # Defining the sensors
    data.define_sensor("Sensor One", "DS18B20", "28-0516929ddeff", 0)
    data.define_sensor("Sensor Two", "DS18B20", "28-0516a43fb9ff", 0)
    try:
        read_in_line_sensor(data)
    finally:    
        data.close()

main()
