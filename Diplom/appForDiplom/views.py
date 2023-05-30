from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .db import create_connection
import json
from .models import *
# Create your views here.

# def index(request):
    # cookie = HttpResponse('<h4>Проверка!</h4>')
    # cookie.set_cookie('personal_id', 123)
    # return cookie

# def index(request):
#     show = request.COOKIES['personal_id']
#     return HttpResponse(f'<h4>Проверка! На куках: {show}</h4>')



# def navigations():
#     return render(request, 'appForDiplom/createTask.html')

def createPractice(request):
    if request.method == "POST":
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return render(request, 'appForDiplom/createPractice.html', {'form': form, 'success': 'Вы успешно добавили практику. Можете загрузить еще одно'})
    else:
        form = PracticeForm()
    return render(request, 'appForDiplom/createPractice.html', {'form': form})


def index(request):
    video = Videos.objects.all()
    test = Test_Question.objects.filter(id_T=1).values('id_Q')
    prac = Practice.objects.all()
    # print(test)
    massive_video = []
    massive_test = []
    massive_practice = []
    number = 1
    for v in video:
        massive_video.append({'number': number, 'pk': v.pk})
        number += 1

    number = 1
    for v in test:
        massive_test.append({'number': number, 'pk': v['id_Q']})
        number += 1
    
    num = 1
    for v in prac:
        massive_practice.append({'number': num, 'pk': v.pk, 'max': v.number})
        num += 1
    # print(massive_test)
    # print(massive_practice)
    context = {
        'videos': massive_video,
        'test': massive_test,
        'practice': massive_practice,
    }
    return render(request, 'appForDiplom/headPage.html', context=context)


def createVideo(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data
            video = Videos()
            video.title = form['comment']
            video.content = form['comment']
            video.video = form['file']
            video.save()

            return render(request, 'appForDiplom/createVideo.html', {'form': form, 'success': 'Вы успешно добавили видео. Можете загрузить еще одно'})
    else:
        form = VideoForm()
    return render(request, 'appForDiplom/createVideo.html', {'form': form})

def createTask(request):
    teacher_lesson = Teacher_Lessons.objects.get(teacher_id = 1, lesson_id = 1)
    id_test = Teacher_Lessons_Test.objects.filter(id_TL = teacher_lesson.id)
    # ИСПРАВИТЬ ТЕСТЫ!!!
    for i in id_test:
        print(i)
    # id_T = Test.objects.filter(pk= id_test.id_test).values('pk','title')
    # choise = []
    # for test in id_T:
    #     choise.append((test['pk'], test['title']))
    choise = []
    print(choise)
    if request.method == "POST":
        form = TaskForm(request.POST)
        print(form)
        if form.is_valid():
            form = form.cleaned_data
            test_id = form['choise']

            new_Question = Question()
            new_Question.q = form['title']
            new_Question.a = f"'{form['answer_1']}','{form['answer_2']}','{form['answer_3']}','{form['answer_4']}'"
            new_Question.r_a = form['correct_answer']
            id_new_question = new_Question.save()
            new_Test = Test_Question()
            new_Test.id_T = test_id
            new_Test.id_Q = id_new_question
            new_Test.save()

            form = TaskForm()
            form.fields['choise'].choices = choise
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'success': 'Вы успешно добавили тест. Можете создать еще один'})

    else:
        form = TaskForm()
        form.fields['choise'].choices = choise
    return render(request, 'appForDiplom/createTask.html', {'form': form})






def laba(request):
    connect = create_connection('/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3')
    cursor = connect.cursor()
    # task = cursor.execute('SELECT * FROM AppForDiplom_question').fetchall()
    video = cursor.execute('SELECT id, title FROM AppForDiplom_videos').fetchall()
    video1 = cursor.execute('SELECT title, id FROM AppForDiplom_videos').fetchall()
    
    if video == video1:
        print('FSDFNDKSJFNDSKFNSD')
    else:
        print('sadkajsndjasndkajs')
    # "SELECT id, name FROM Student"
    # |1|adsdasdsadas| -> json_massive
    # "SELECT name, id FROM Student"
    # |adsdasdsadas|1| -> json_massive
    # json_string = {
    #     'task': [],
    #     'video': [],
    # }
    # # sss['task'] = {}
    # number = 0
    # # json_string['task'][number]
    # for i in task:
    #     txt = i[2]
    #     txt = txt.split(',')
    #     s = {
    #         'number': number + 1,
    #         'q': i[1],
    #         'var': txt,
    #         'answer': i[3]
    #     }
    #     json_string['task'].append(s)
    #     number = number + 1
    #     # print(i[1])
    # # print('sdfsd')
    # number = 0
    # # print(video)
    # for i in video:
    #     s = {
    #         'name': number + 1,
    #         'scr': i[4],
    #     }
    #     json_string['video'].append(s)
    #     number = number + 1

    # return render(request, 'appForDiplom/lab.html', {'json_string': json_string})

def practice(request, id):
    prac = Practice.objects.get(pk = id)
    
    form = DoPracticeForm()
    context = {
        "title": prac.title, 
        "text": prac.content,
        "number": prac.number,
        'id': id,
        'form': form,
        'success': '',
    }
    
    if request.method == "POST":
        f = open(prac.practice.path, 'r')
        fromView = request.POST['do']
        # print(fromView)
        # ОТПРАВЛЯЕМ 2 ЗАПРОСА НА ТЕСТОВУЮ БД ПОЛУЧАЕМ РЕЗУЛЬТАТА И СРАВНИВАЕМ!
        if fromView == f.read():
            context['success'] = 'Поздравляем! Вы сдали данную практику'
            return render(request, 'appForDiplom/prac.html', context=context)
        else:
            context['success'] = 'Попытайтесь еще раз!'
            context['form'] = DoPracticeForm(initial={'do': fromView})
            return render(request, 'appForDiplom/prac.html', context=context)
    
    return render(request, 'appForDiplom/prac.html', context=context)

def lection(request, id):
    video = Videos.objects.get(pk=id)
    context = {
        'type': 'Видео материал',
        'name': video.title,
        'video_url': video.video,
        'date_create': video.created_at
    }
    return render(request, 'appForDiplom/video.html', context=context)