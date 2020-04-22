from django.contrib import admin
from .models import User, Student, Teacher

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'first_name', 'last_name')
    
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id', 'user_id', 'subject_id')
    
class StudentAdmin(admin.ModelAdmin):
    list_display=('username', 'user_id', 'class_id')

admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
