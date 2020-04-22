from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from classes.models import Class, Subject
from users.models import User, Student

def get_classes_list(request):
    if "GET" == request.method:
        classes = Class.object.all().values('parallel', 'letter')
        return JsonResponse({
            'Список классов': list(classes)
            })
    return HttpResponseNotAllowed(['GET'])


def get_students_list(request, class_name):
    if "GET" == request.method:
        class_id = get_object_or_404(Class, name=class_name).id
        students = Student.objects.filter(class_name=class_id).values('user_id')
        students_list = list(students)
        response = []
        for student in students_list:
            user = User.objects.filter(id=student.user_id).values('first_name', 'last_name')
            response.append(user)
        return JsonResponse({'Список учеников': response})
    return HttpResponseNotAllowed(['GET'])


def get_subjects_list(request):
    if "GET" == request.method:
        subjects = Subject.object.all().values('name', 'class_name')
        return JsonResponse({
            'Список предметов': list(subjects)
            })
    return HttpResponseNotAllowed(['GET'])