from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    contents = models.TextField(max_length=1000, blank=True)
    students = models.ManyToManyField(
        Student, blank=True, through='Enrollment')

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
