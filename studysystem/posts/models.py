from django.db import models

class Posts(models.Model):
    topic = models.TextField(verbose_name='Тема поста')
    author = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, verbose_name="id пользователя")
    content = models.TextField(verbose_name='Текст поста')
    added_at = models.DateTimeField(verbose_name='Время отправки', null=False, auto_now=True)
    for_class = models.ForeignKey('classes.Class', on_delete=models.CASCADE, verbose_name="id класса")
    subject = models.ForeignKey('classes.Subject', on_delete=models.CASCADE, verbose_name="id предмета")

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comments(models.Model):
    post = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name="id поста")
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="id пользователя")
    content = models.TextField(verbose_name='Текст комментария')
    added_at = models.DateTimeField(verbose_name='Время отправки', null=False, auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
