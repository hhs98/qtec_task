from django.shortcuts import render
from .models import *


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'core/index.html', context)
