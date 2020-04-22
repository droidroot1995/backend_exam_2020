from django.db import models

class Class(models.Model):
    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'

    parallel = models.IntegerField(verbose_name='номер параллели')
    letter = models.CharField(max_length=1, verbose_name='буква класса')
    teacher = models.ForeignKey(
        'users.Teacher',
        on_delete=models.PROTECT,
        verbose_name='классный руководитель'
    )
    
class Subject(models.Model):
    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    name = models.CharField(max_length=32, verbose_name='название предмета')
    class_name = models.ForeignKey(
        'Class',
        on_delete=models.PROTECT,
        verbose_name='класс, которому преподаётся данный предмет'
    )
