from django import forms
from .models import User, Teacher, Student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_teacher', 'first_name', 'last_name']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'class_name']
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject']