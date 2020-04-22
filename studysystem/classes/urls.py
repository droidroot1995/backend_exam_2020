from django.contrib import admin
from django.urls import path
from classes.views import get_classes_list, get_students_list, get_subjects_list

urlpatterns = [
    path('subjects/', get_subject_list, name='subjects list'),
    path('classes/', get_classes_list, name='classes list'),
    path('<string:class_name>', get_students_list, name='students list'),
]