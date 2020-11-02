from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('course/<str:pk>', views.course_detail),
    path('add-course', views.add_course),
    path('update-course/<str:pk>', views.update_course),
    path('enroll/<str:pk>', views.enroll),
    path('login', views.login_page),
    path('logout', views.logoutUser),
    path('signup', views.register_student),
    path('teacher', views.register_teacher),
]
