from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http  import require_GET, require_POST

from django.apps import apps

from .forms import UserForm, StudentForm, TeacherForm

# Create your views here.

@csrf_exempt
@require_POST
def create_user(request):
    User = apps.get_model('users', 'User')
    
    form = UserForm(request.POST)
    
    
    if form.is_valid():
        user = form.save()
        usr = {'id': user.id, 'username': user.username, 'first_name': user.first_name, 
               'last_name': user.last_name, 'is_teacher': user.is_teacher}
        
        return JsonResponse({'user': usr})

    return JsonResponse({'error': form.errors}, status=400)
    
    

@csrf_exempt
@require_POST
def create_student(request):
    User = apps.get_model('users', 'User')
    Student = apps.get_model('users', 'Student')
    
    form = StudentForm(request.POST)
    
    if form.is_valid():
        student = Student.objects().filter(user_id=form.cleaned_data['user_id']).first()
        
        if student == None:
            student = form.save()
            
        stud = {'id': student.id, 'user_id': student.user.id, 'class_name_id': student.class_name.id}
            
        return JsonResponse({'student': student})
    
    return JsonResponse({'error': form.errors}, status=400)
    
    
    
@csrf_exempt
@require_POST
def create_teacher(request):
    User = apps.get_model('users', 'User')
    Teacher = apps.get_model('users', 'Student')
    
    form = TeacherForm(request.POST)
    
    if form.is_valid():
        teacher = Teacher.objects().filter(user_id=form.cleaned_data['user_id']).first()
        
        if teacher == None:
            teacher = form.save()
            
        teach = {'id': teacher.id, 'user_id': teacher.user.id, 'subject_id': teacher.subject.id}
            
        return JsonResponse({'teacher': teach})
    
    return JsonResponse({'error': form.errors}, status=400)


@require_GET
def students_list(request):
    User = apps.get_model('users', 'User')
    Student = apps.get_model('users', 'Student')
    Class = apps.get_model('classes', 'Class')
    
    students = Student.objects().all().values('id', 'user_id', 'class_id')
    
    result = []
    
    for s in students:
        user = User.objects().filter(id=s['user_id']).first()
        s_class = Class.objects().filter(id=s['class_name_id'])
        
        student = {'id': s.id, 'first_name': user.first_name, 'last_name': user.last_name,
                   'class_number': s_class.parallel, 'class_letter': s_class.letter}
        
        result.append(student)
        
    return JsonResponse({'students': result})

@require_GET
def teachers_list(request):
    User = apps.get_model('users', 'User')
    Teacher = apps.get_model('users', 'Student')
    Subject = apps.get_model('classes', 'Subject')
    
    teachers = Teacher.objects().all().values('id', 'user_id', 'subject_id')
    
    result = []
    
    for t in teachers:
        user = User.objects().filter(id=t['user_id']).first()
        subject = Subject.objects().filter(id=t['subject_id'])
        
        teacher = {'id': t.id, 'first_name': user.first_name, 'last_name': user.last_name,
                   'subject_name': subject.name, 'subject_class': subject.class_name.id}
        
        result.append(teacher)
        
    return JsonResponse({'teachers': result})

@require_GET
def search_by_name(request):
    User = apps.get_model('users', 'User')
    
    users = User.objects.filter(username__contains=request.GET['name']).values('id', 'username', 'first_name', 'last_name')[:int(request.GET['limit'])]
    return JsonResponse({'users': list(users)})

@require_GET
def search_by_id(request):
    User = apps.get_model('users', 'User')
    
    users = User.objects.filter(id=request.GET['id']).values('id', 'username', 'first_name', 'last_name')[:int(request.GET['limit'])]
    return JsonResponse({'users': list(users)})