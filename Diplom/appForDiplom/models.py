from django.db import models

# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', blank=False)
    content = models.TextField(verbose_name='Дополнительный материал', blank=False)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации') #auto_now_add -> ставит время создания и больше его не трогает
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') #auto_now -> ставит время обновления в бд и меняет его при каждом измнении
    #video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)
    video = models.TextField(verbose_name='Видео', blank=True)


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

class Practice(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название практики')
    content = models.TextField(verbose_name='Задание для практики', blank=False, default=' ')
    number = models.IntegerField(verbose_name='Максимальное количество баллов', default=10)
    practice = models.FileField(upload_to='practice/%Y/%m/%d/', verbose_name='Файл с правильными запросами', blank=True)
    # created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации') 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Практика'
        verbose_name_plural = 'Практики'

class Lessons(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название предмета')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'

class Teacher_Lessons(models.Model):
    teacher_id = models.IntegerField(verbose_name='ID_преподавателя')
    lesson_id = models.IntegerField(verbose_name='ID_урока')

class Question(models.Model):
    q = models.CharField(max_length=255, verbose_name='Вопрос')
    a_1 = models.TextField(verbose_name='Вариант ответ №1', default='-')
    a_2 = models.TextField(verbose_name='Вариант ответ №2', default='-')
    a_3 = models.TextField(verbose_name='Вариант ответ №3', default='-')
    a_4 = models.TextField(verbose_name='Вариант ответ №4', default='-')
    r_a = models.CharField(max_length=255, verbose_name='Правильный ответ')
    number = models.IntegerField(verbose_name='Максимальное количество баллов', default=1)

    def __str__(self):
        return self.q

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название теста'
        verbose_name_plural = 'Название тестов'

class Test_Question(models.Model):
    id_T = models.IntegerField(verbose_name='ID Теста')
    id_Q = models.IntegerField(verbose_name='ID Вопроса')
    
    class Meta:
        verbose_name_plural = 'Таблица связей тесты_вопросы'

class Teacher_Lessons_Video(models.Model):
    id_video = models.IntegerField(verbose_name='ID видео')
    id_TL = models.IntegerField(verbose_name='ID преподаватель_предмет')

    class Meta:
        verbose_name_plural = 'Таблица связей Преподаватель_Предмет_Видео'


class Teacher_Lessons_Test(models.Model):
    id_test = models.IntegerField(verbose_name='ID теста')
    id_TL = models.IntegerField(verbose_name='ID преподаватель_предмет')

    class Meta:
        verbose_name_plural = 'Таблица связей Преподаватель_Предмет_Тест'


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО студента')

class User_Test(models.Model):
    id_user = models.IntegerField(verbose_name='ID студента')
    id_test = models.IntegerField(verbose_name='ID теста')
    json_massive = models.TextField(verbose_name='JSON_массив с информацией об тесте')
