from django import forms
from django.forms import ModelForm

from .models import *


class CourseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    cost = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    contents = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Course
        fields = '__all__'
