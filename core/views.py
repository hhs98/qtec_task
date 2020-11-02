from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'core/index.html', context)


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    students = course.students.all()
    hasib = Student.objects.get(pk=request.user.student.id)
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
    form = CourseForm(initial={'teacher': request.user.teacher.id})
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


def enroll(request, pk):
    course = Course.objects.get(id=pk)
    student = Student.objects.get(id=request.user.student.id)
    course.students.add(student)
    return redirect(course_detail, pk=pk)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'core/login.html')


def register_student(request):
    form = CreateUserForm()
    studentForm = StudentForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        studentForm = StudentForm(request.POST)
        if form.is_valid() and studentForm.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect(index)

    context = {'form': form, 'studentForm': studentForm}
    return render(request, 'core/signup.html', context)


def register_teacher(request):
    form = CreateUserForm()
    teacherForm = StudentForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        teacherForm = TeacherForm(request.POST)
        if form.is_valid() and teacherForm.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            teacher = teacherForm.save(commit=False)
            teacher.user = user
            teacher.save()
            login(request, user)
            return redirect(index)

    context = {'form': form, 'teacherForm': teacherForm}
    return render(request, 'core/signup_teacher.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')
