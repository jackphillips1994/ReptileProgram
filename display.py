# Module that handles displaying the data to the console and LCD screen

from main import *
import time

data = SensorData()

data.define_sensor("Sensor One", "DS18B20", "28-0516929ddeff", 0)
data.define_sensor("Sensor Two", "DS18B20", "28-0516a43fb9ff", 0)

try:
    while True:
        for sensor in data.get_sensors():
            while button_pressed(GPIO_list['button']) != True:
                sensor_name, temperature, reading_time = read_in_line_sensor(sensor)
                print("Sensor {0} current reading is: {1}".format(sensor_name, temperature))
                LCD_display(sensor_name, temperature)
            time.sleep(1.0)
except KeyboardInterrupt:
    print("Program exited correctly")
    data.close()
    exit()
