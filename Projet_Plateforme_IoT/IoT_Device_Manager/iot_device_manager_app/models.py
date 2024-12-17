from django.db import models

# Create your models here.
class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    longi = models.FloatField()  # Longitude
    lati = models.FloatField()  # Latitude
    period = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name