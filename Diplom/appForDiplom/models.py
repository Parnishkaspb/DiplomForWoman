from django.db import models

# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(verbose_name='Дополнительный материал', blank=False)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации') #auto_now_add -> ставит время создания и больше его не трогает
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') #auto_now -> ставит время обновления в бд и меняет его при каждом измнении
    video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class Teacher(models.Model):
    title = models.CharField(max_length=255, verbose_name='ФИО')

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

class Teacher_Lessons(models.Model):
    teacher_id = models.IntegerField(verbose_name='ID_преподавателя')
    lesson_id = models.IntegerField(verbose_name='ID_урока')

class Question(models.Model):
    q = models.CharField(max_length=255, verbose_name='Вопрос')
    a = models.TextField(verbose_name='Варианты ответов')
    r_a = models.CharField(max_length=255, verbose_name='Правильный ответ')

    def __str__(self):
        return self.q

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'