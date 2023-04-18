from django.db import models

# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.JSONField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации') #auto_now_add -> ставит время создания и больше его не трогает
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') #auto_now -> ставит время обновления в бд и меняет его при каждом измнении
    photo = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class Teacher(models.Model):
    title = models.CharField(max_length=255, verbose_name='ФИО')
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT, verbose_name='Предмет', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'



class Lessons(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название предмета')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'
# class WatchLessons(models.Model):
