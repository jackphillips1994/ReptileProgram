from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

import model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['MODEL'] = model.SensorData()

admin = Admin(app, name='Reptile Monitoring', template_mode='bootstrap3', url='/')
admin.add_view(ModelView(model.Sensor))
admin.add_view(ModelView(model.SensorReading))