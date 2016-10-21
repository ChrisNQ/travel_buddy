from django.shortcuts import render, redirect
import datetime
from .models import Travel
from ..loginreg.models import User
# Create your views here.

def index(request):
    context = {
        'travels': Travel.objects.all()
    }
    return render(request, 'travels/index.html', context)

def add(request):
    return render(request, 'travels/add.html')

def create(request):
    # Travel.objects.create(description = request.POST['description'], destination = request.POST['destination'])
    return render(request, 'travels/index.html')


def validate(request):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return render(request, 'travels/index.html')
