# Python file that contains the sensor class
# More than temperature sensors can be added to this program

from peewee import *

# Defining the database
db = SqliteDatabase('reptile.db', check_same_thread=False)

# Classes to handle talking to the DB Tables
class Sensor(Model):
    name = CharField()
    device_id = CharField()
    device_type = CharField()
    pin = CharField()

    class Meta:
        database = db

class SensorReading(Model):
    time = DateTimeField()
    name = CharField()
    reading = FloatField()

    class Meta:
        database = db


class SensorData(object):

    def __init__(self):
        db.connect()
        db.create_tables([Sensor, SensorReading], safe=True)

    def define_sensor(self, name, device_type, device_id, pin):
        Sensor.get_or_create(name=name, device_type=device_type, device_id=device_id, pin=pin)

    def get_sensors(self):
        return Sensor.select()

    def get_recent_readings(self, name, limit=30):
        return SensorReading.select() \
                            .where(SensorReading.name == name) \
                            .order_by(SensorReading.time.desc()) \
                            .limit(limit)

    def add_reading(self, time, name, reading):
        SensorReading.create(time=time, name=name, reading=reading)

    def close(self):
        db.close()
