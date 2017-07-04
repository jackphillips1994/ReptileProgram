# Module that handles storing the temperature readings in the database

from main import *

# Stores the current reading of the each of the temperature sensors every
# three seconds

data = SensorData()

try:
    while True:
        for sensor in data.get_sensors():
            sensor_name, temperature, reading_time = read_in_line_sensor(sensor)
            data.add_reading(reading_time, sensor_name, temperature)
            time.sleep(3.0)
except KeyboardInterrupt:
    print("Program exited correctly")
    data.close()
    exit()
