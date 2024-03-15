from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello_view(request):
    return HttpResponse("Hello! Its my project")

current_date = datetime.now()
def current_data_view(request):
    return HttpResponse(current_date)

def goodbye_view(request):
    return HttpResponse("Goodbye user!")