from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('course/<str:pk>', views.course_detail),
    path('add-course', views.add_course),
    path('update-course/<str:pk>', views.update_course),
]
