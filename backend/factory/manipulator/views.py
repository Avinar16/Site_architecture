from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import sys
import json
from .models import Report
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .classes.Grid import factory_grid
from .classes.Manipulator import manipulator


@csrf_exempt
def move(request):
    data = json.loads(request.body)
    manipulator.move(data['command'])
    return HttpResponse('', status=200)


@csrf_exempt
def grab(request):
    manipulator.grab()
    return HttpResponse('', status=200)


@csrf_exempt
def load_grid(request):
    data_string = grid_state_to_string(factory_grid)
    return JsonResponse({'data': data_string})


@csrf_exempt
def load_save(request):
    data = json.loads(request.body)['name']
    print(data, file=sys.stderr)
    report = Report.objects.get(name=data)
    manipulator.load_grid(report.text)
    return HttpResponse('', status=200)


@csrf_exempt
def send_report(request):
    data = json.loads(request.body)
    data_string = grid_state_to_string(factory_grid)
    report = Report()
    try:
        report.name = data['name']
        report.text = data_string
        report.reg_date = datetime.now()
        report.save()
        print(data, file=sys.stderr)
        return HttpResponse('', status=200)
    except:
        report.save()
        report.delete()
        return HttpResponse('', status=400)


@csrf_exempt
def get_reports(request):
    reports = Report.objects.all()
    reports_json = serialize('json', reports, fields=('name', 'text'))
    reports_list = json.loads(reports_json)
    print(reports_list, file=sys.stderr)
    return JsonResponse(reports_list, safe=False)


def grid_state_to_string(grid):
    data_string = ''
    for row in grid:
        for element in row:
            data_string += str(element)
    return data_string
