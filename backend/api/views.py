import random

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .models import Story
import sys

# Create your views here.
@csrf_exempt
def get_joke(request):
    if request.method == "GET":
        story = Story.objects.order_by('?').first()
        print(story, file=sys.stderr)
        return JsonResponse({"body": f"{story}"})
    elif request.method == "POST":
        data = json.loads(request.body)
        print(data, file=sys.stderr)
        story = Story(text=f'{data}')
        story.save()
        return JsonResponse({'body': f"Data recieved"})
