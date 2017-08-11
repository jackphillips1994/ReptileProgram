from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

import model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['MODEL'] = model.SensorData()
app.debug = True

admin = Admin(app, name='Reptile Monitoring', template_mode='bootstrap3', url='/')
# TODO: Change the names in the menu to something that makes sense
admin.add_view(ModelView(model.Sensor))
admin.add_view(ModelView(model.SensorReading))