from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'core/index.html', context)


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    students = course.students.all()
    hasib = Student.objects.get(pk=1)
    try:
        if hasib.course_set.get(id=pk):
            enrolled = True
        else:
            enrolled = False
    except Course.DoesNotExist:
        enrolled = False
    context = {'course': course, 'students': students, 'enrolled': enrolled}
    return render(request, 'core/course_detail.html', context)


def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'core/add_course.html', context)


def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'core/add_course.html', context)
