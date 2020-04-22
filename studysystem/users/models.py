from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
        
class Student(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    class_name = models.ForeignKey("classes.Class", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        
class Teacher(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    subject = models.ForeignKey("classes.Subject", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'