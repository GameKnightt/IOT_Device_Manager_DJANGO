import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor, Unit, Measure
from .forms import SensorForm, UnitForm
from django.utils import timezone
from datetime import timedelta
from django.db.models import Max, Min, Avg
from django.core.serializers.json import DjangoJSONEncoder

##########################################################################################
##########################################################################################

def sensor_visualization(request, pk=None):
    sensors = Sensor.objects.all()
    
    # Get selected sensor or default to first one
    selected_sensor_id = request.GET.get('sensor_id')
    if selected_sensor_id:
        selected_sensor = Sensor.objects.get(pk=selected_sensor_id)
    else:
        selected_sensor = sensors.first() 
    
    # Get measurements for selected sensor
    measurements = Measure.objects.filter(sensor=selected_sensor).order_by('timestamp')
    
    # Prepare data for chart
    timestamps = [m.timestamp.strftime("%Y-%m-%d %H:%M:%S") for m in measurements]
    values = [float(m.value) for m in measurements]

    context = {
        'sensors': sensors,
        'selected_sensor': selected_sensor,
        'timestamps': json.dumps(timestamps),
        'values': json.dumps(values),
    }
    return render(request, 'sensor_visualization.html', context)

##########################################################################################
##########################################################################################

def sensor_list(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensor_list.html', {'sensors': sensors})

def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'unit_list.html', {'units': units})

##########################################################################################

def sensor_detail(request, pk):
    sensor = Sensor.objects.get(pk=pk)
    stats = Measure.objects.filter(sensor=sensor).aggregate(
        max_value=Max('value'),
        min_value=Min('value'),
        avg_value=Avg('value')
    )
    return render(request, 'sensor_detail.html', {
        'sensor': sensor,
        'stats': stats
    })  

##########################################################################################

def unit_detail(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    return render(request, 'unit_detail.html', {'unit': unit})

##########################################################################################

def sensor_create(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    return render(request, 'sensor_form.html', {'form': form})

##########################################################################################

def unit_create(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = UnitForm()
    return render(request, 'unit_form.html', {'form': form})

##########################################################################################

def sensor_update(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('sensor_detail', pk=sensor.pk)
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'sensor_form.html', {'form': form})

##########################################################################################

def unit_update(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_detail', pk=unit.pk)
    else:
        form = UnitForm(instance=unit)
    return render(request, 'unit_form.html', {'form': form})

##########################################################################################

def sensor_delete(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        sensor.delete()
        return redirect('sensor_list')
    return render(request, 'sensor_confirm_delete.html', {'sensor': sensor})

##########################################################################################

def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_list')
    return render(request, 'unit_confirm_delete.html', {'unit': unit})

##########################################################################################
##########################################################################################