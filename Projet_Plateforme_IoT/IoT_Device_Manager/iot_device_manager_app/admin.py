from django.contrib import admin
from .models import Sensor, Measure, Unit, Metric

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Measure)
admin.site.register(Unit)
admin.site.register(Metric)
