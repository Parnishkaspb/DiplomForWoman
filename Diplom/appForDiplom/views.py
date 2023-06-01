from django.shortcuts import render, redirect
from .forms import *
from .db import create_connection
from .models import *

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
    
    choise_ss = []
    for i in id_test:
        id_T = Test.objects.filter(pk= i.id_test).values('pk','title')
        choise_ss.append(id_T)

    choise = []
    for test in choise_ss:
        choise.append({'id': test[0]['pk'], 'title': test[0]['title']})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            test_id = request.POST['choise']
            new_Question = Question()
            new_Question.q = form['title']
            new_Question.a = f"'{form['answer_1']}','{form['answer_2']}','{form['answer_3']}','{form['answer_4']}'"
            new_Question.r_a = form['correct_answer']
            new_Question.save()
            new_Test = Test_Question()
            new_Test.id_T = int(test_id)
            new_Test.id_Q = new_Question.id
            new_Test.save()

            form = TaskForm()
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'success': 'Вы успешно добавили тест. Можете создать еще один'})
        else:
            form = TaskForm()
            form.fields['choise'].choices = choise
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'success': 'К сожалению произошла ошибка'})
    else:
        form = TaskForm()
    return render(request, 'appForDiplom/createTask.html', {'form': form, 'choise': choise})


def test(request, id):
    test_name = Test.objects.get(pk=id)
    test_ques = Test_Question.objects.filter(id_T = id).values('id_Q')
    massiveWithQuestion = []
    number = 1
    for i in test_ques:
        massiveWithQuestion.append({'id': i['id_Q'], 'number': number})
        number += 1
    
    # print(massiveWithQuestion)
    context = {
        'massiveWithQuestion': massiveWithQuestion,
        'type': 'Тест',
        'name': test_name,
    }

    return render(request, 'appForDiplom/test.html', context=context)

def test_check(request, id):
    test_ques = Test_Question.objects.filter(id_Q = id).values('id_T').first()
    question = Question.objects.get(pk=id)
    question_answers = question.a.split(',')
    context = {
        'name_question': question.q,
        'question_answers': question_answers,
        'main_test_id': test_ques['id_T'],
        'id_question': id,
        'right': 0,
        'no_right': 0,
        'no_right_on': 0
    }
    if request.method == "POST":
        right_answers = question.r_a
        answer = request.POST['question'] 
        if answer == right_answers:
            context['right'] = 1
            return render(request, 'appForDiplom/test_chech.html', context=context)
        else:
            context['right'] = -1
            render(request, 'appForDiplom/test_chech.html', context=context)

    return render(request, 'appForDiplom/test_chech.html', context=context)

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

        # ПОМЕНЯТЬ НА СВОЙ ПУТЬ!!!!
        connect = create_connection('/Users/bogdankrasnikov/Desktop/NastyaDiplom/Diplom/db.sqlite3')

        cursor = connect.cursor()
        your_select = cursor.execute(f.read()).fetchall()
        teacher_select = cursor.execute(fromView).fetchall()        
        if your_select == teacher_select:
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