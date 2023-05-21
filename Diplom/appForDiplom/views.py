from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .db import create_connection
import json
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




def index(request):
    # if request.POST 
    # return render(request, 'appForDiplom/tes.html')
    return render(request, 'appForDiplom/start.html')



def handle_uploaded_file(f):  
    string = 'Diplom/video'+f.name
    with open(string, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)
    return string


def createVideo(request):
    if request.method == "POST":
        # print(request.FILES)
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = VideoForm()
            return render(request, 'appForDiplom/createVideo.html', {'form': form, 'success': 'Вы успешно добавили видео. Можете загрузить еще одно'})
    else:
        form = VideoForm()
    return render(request, 'appForDiplom/createVideo.html', {'form': form})

def createTask(request):
    if request.method == "POST":
        # print(request.FILES)
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            answer = f"'{form['answer_1']}','{form['answer_2']}','{form['answer_3']}','{form['answer_4']}'"
            connect = create_connection("/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3")
            cursor = connect.cursor()
            title = form['title']
            correct_answer = form['correct_answer']
            sqlInsertInto = f'INSERT INTO AppForDiplom_question (q,a,r_a) VALUES ("{title}", "{answer}", "{correct_answer}")'
            print(sqlInsertInto)
            cursor.execute(sqlInsertInto)
            connect.commit()
            form = TaskForm()
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'success': 'Вы успешно добавили тест. Можете создать еще один'})
    else:
        form = TaskForm()
    return render(request, 'appForDiplom/createTask.html', {'form': form})






def laba(request):
    connect = create_connection('/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3')
    cursor = connect.cursor()
    task = cursor.execute('SELECT * FROM AppForDiplom_question').fetchall()
    video = cursor.execute('SELECT * FROM AppForDiplom_videos').fetchall()

    json_string = {
        'task': [],
        'video': [],
    }
    # sss['task'] = {}
    number = 0
    # json_string['task'][number]
    for i in task:
        txt = i[2]
        txt = txt.split(',')
        s = {
            'number': number + 1,
            'q': i[1],
            'var': txt,
            'answer': i[3]
        }
        json_string['task'].append(s)
        number = number + 1
        # print(i[1])
    # print('sdfsd')
    number = 0
    # print(video)
    for i in video:
        s = {
            'name': number + 1,
            'scr': i[4],
        }
        json_string['video'].append(s)
        number = number + 1

    return render(request, 'appForDiplom/lab.html', {'json_string': json_string})

def practice(request):
    json_string = {
        "text":"<h1> Добро пожаловать </h1>", 
        "task": [
            {
                'number': '1',
                'q':'Создать таблицу под названием <strong>DB</strong> следующей структуры: <table border="1" cellpadding="1" cellspacing="1"><tr><td>Поле</td><td>Тип, описание</td></tr><tr><td><strong>ID</strong></td><td>INT PRIMARY KEY AUTO_INCREMENT</td></tr></table>'
            }
        ]
    }

    if request.method == "POST":
        f = open('first_practice.txt', 'r')
        fromView = request.POST['first_practice']
        if f.read() == fromView:
            print('All good')
            return render(request, 'appForDiplom/good.html')
        else:
            return render(request, 'appForDiplom/prac.html', {'json_string': json_string}) # СЮДА ДОБАВИТЬ ДАННЫЕ ИЗ TEXTAREA ЧТОБЫ ЧЕЛОВЕК НЕ ПЕРЕВВОДИЛ ДАННЫЕ!!!!!
    
    return render(request, 'appForDiplom/prac.html', {'json_string': json_string})

def lection(request):
    connect = create_connection('/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3')
    cursor = connect.cursor()
    video = cursor.execute('SELECT * FROM AppForDiplom_videos').fetchall()
    task = cursor.execute('SELECT * FROM AppForDiplom_question').fetchall()
    print(video)
    print(task)
    connect = create_connection('/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3')
    cursor = connect.cursor()
    task = cursor.execute('SELECT * FROM AppForDiplom_question').fetchall()
    video = cursor.execute('SELECT * FROM AppForDiplom_videos').fetchall()

    json_string = {
        'task': [],
        'video': [],
    }
    # sss['task'] = {}
    number = 0
    # json_string['task'][number]
    for i in task:
        txt = i[2]
        txt = txt.split(',')
        s = {
            'number': number + 1,
            'q': i[1],
            'var': txt,
            'answer': i[3]
        }
        json_string['task'].append(s)
        number = number + 1
        # print(i[1])
    # print('sdfsd')
    number = 0
    # print(video)
    for i in video:
        s = {
            'name': number + 1,
            'scr': i[4],
        }
        json_string['video'].append(s)
        number = number + 1
        

    return render(request, 'appForDiplom/video.html', {'json_string': json_string})