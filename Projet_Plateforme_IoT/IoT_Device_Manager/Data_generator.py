import random
from datetime import datetime, timedelta
from iot_device_manager_app.models import Metric, Unit, Sensor, Measure
from tqdm import tqdm

import warnings

# Suppress Django RuntimeWarning for naive datetime
warnings.filterwarnings(
    "ignore",
    message=r"DateTimeField .* received a naive datetime",
    category=RuntimeWarning,
)

# Define the list of metrics and units
metrics_units = {
    "Distance": ["Meter", "Kilometer"],
    "Pressure": ["Pascal", "Bar"],
    "Temperature": ["Celsius", "Kelvin", "Fahrenheit"],
    "Noise": ["Decibel"],
    "Speed": ["Meter/second", "Kilometer/hour"],
    "Luminosity": ["Lux", "Candela"],
    "Pollution": ["CO2/Kg"],
    "Energy Consumption": ["Joule", "Kilowatt-hour"],
    "Humidity": ["Percentage"],
    "Wind Direction": ["Degree"],
    "Vibration": ["Hertz"],
}

# Locations
locations = [
    ("Nantes", 47.2184, -1.5536),
    ("Rennes", 48.1173, -1.6778),
    ("IUT de Carquefou", 47.2980, -1.5013),
]

# Measurement range
value_range = {
            "Distance": (0, 1000),
            "Pressure": (1000, 101325),
            "Temperature": (-50, 50),
            "Noise": (0, 150),
            "Speed": (0, 120),
            "Luminosity": (0, 100000),
            "Pollution": (0, 500),
            "Energy Consumption": (0, 1000),
            "Humidity": (0, 100),
            "Wind Direction": (0, 360),
            "Vibration": (0, 100),
        }

# Latitude and longitude variation parameter
lat_lon_variation = 0.1

MEASUREMENT_SAMPLE_NUMBER = 1000
SENSORS_NUMBER = 1000

# Generate Metrics
metric_objs = {}
for metric_name in metrics_units.keys():
    metric = Metric.objects.create(name=metric_name)
    metric_objs[metric_name] = metric

# Generate Units
unit_objs = {}
for metric_name, unit_list in metrics_units.items():
    metric = metric_objs[metric_name]
    for unit_name in unit_list:
        unit = Unit.objects.create(name=unit_name, metric=metric)
        unit_objs[f"{metric_name}-{unit_name}"] = unit

# Generate Sensors
sensors = []
for _ in tqdm(range(SENSORS_NUMBER)):
    location_name, base_lat, base_lon = random.choice(locations)
    lat = base_lat + random.uniform(-lat_lon_variation, lat_lon_variation)
    lon = base_lon + random.uniform(-lat_lon_variation, lat_lon_variation)
    unit = random.choice(list(unit_objs.values()))
    period = random.choice([1, 5, 10, 15, 30, 60])  # Period in minutes
    sensor_name = f"Sensor {unit.metric.name} {unit.name} {location_name}"
    sensor = Sensor.objects.create(name=sensor_name, longi=lon, lati=lat, period=period, unit=unit)
    sensors.append(sensor)

# Generate Measures
start_date = datetime.now() - timedelta(days=30)
for sensor in tqdm(sensors):
    current_time = start_date
    measures = []
    for _ in range(MEASUREMENT_SAMPLE_NUMBER):  # 1000 measurements per sensor
        metric_name = sensor.unit.metric.name
        value = round(random.uniform(*value_range[metric_name]), 2)
        measure = Measure(
            sensor=sensor,
            value=value,
            timestamp=current_time
,
        )
        measures.append(measure)
        current_time += timedelta(minutes=sensor.period)
    Measure.objects.bulk_create(measures) 

