from django.shortcuts import render, redirect
from .forms import *
from .db import create_connection
from .models import *
import json

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
    test = Teacher_Lessons_Test.objects.filter(id_TL=1).values('id_test')
    # print(test)
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
        userTest = User_Test.objects.filter(id_test = v['id_test']).values('json_massive')
        try:
            json_array = userTest[0]['json_massive']
            json_array = json_array.replace("'", '"')
            json_array = json.loads(json_array)
            your_point = json_array[len(json_array)-2]['finalMark']
            max_point = json_array[len(json_array)-1]['totalMark']
        except:
            max_point = 0
            your_point = 0
        # print(userTest)
        # for test in userTest:
        #     print('adaskjnas')
        #     print(test)
        massive_test.append({'number': number, 'pk': v['id_test'], 'max': max_point, 'your': your_point})
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
        form = VideoForm(request.POST)
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
        choise.append({'id': int(test[0]['pk']), 'title': test[0]['title']})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            test_id = request.POST['choise']
            new_Question = Question()
            new_Question.q = form['title']
            new_Question.a_1 = form['answer_1']
            new_Question.a_2 = form['answer_2']
            new_Question.a_3 = form['answer_3']
            new_Question.a_4 = form['answer_4']
            new_Question.r_a = form['correct_answer']
            new_Question.save()
            new_Test = Test_Question()
            new_Test.id_T = int(test_id)
            new_Test.id_Q = new_Question.id
            new_Test.save()

            form = TaskForm(initial={'what_theme': int(test_id)})
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'test_id': int(test_id), 'success': 'Вы успешно добавили тест. Можете создать еще один',  'choise': choise})
        else:
            form = TaskForm(initial={'what_theme': int(test_id)})
            return render(request, 'appForDiplom/createTask.html', {'form': form, 'test_id': int(test_id), 'success': 'К сожалению произошла ошибка',  'choise': choise})
    else:
        test_id = 0
        form = TaskForm(initial={'what_theme': int(test_id)})
    return render(request, 'appForDiplom/createTask.html', {'form': form, 'choise': choise, 'test_id': int(test_id)})


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
    # id_student передается в pro.guap через куки
    what_do = 0
    id_student = 1
    test_ques = Test_Question.objects.filter(id_Q = id).values('id_T').first()
    questions_id = Test_Question.objects.filter(id_T = test_ques['id_T']).values('id_Q')

    infoAboutTest = User_Test.objects.filter(id_user = id_student, id_test = test_ques['id_T']).first()
    if infoAboutTest is None:
        tmp_massive = []
        total_mark = 0
        for i in questions_id:
            tmp_id =i['id_Q']
            tmp = Question.objects.filter(id = tmp_id).values('number').first()
            total_mark = total_mark + tmp['number']
            tmp_massive.append({
                "id_Q": tmp_id,
                "mark": -1
            })
        tmp_massive.append({
                "finalMark": 0,
            })
        tmp_massive.append({
                "totalMark":total_mark
            })
        newUserTest = User_Test(
            id_user=id_student,
            id_test=test_ques['id_T'],
            json_massive=tmp_massive
        )
        newUserTest.save()
        json_array = tmp_massive
    else: 
        json_array = infoAboutTest.json_massive
        json_array = json_array.replace("'", '"')
        json_array = json.loads(json_array)
        for i in range(0, len(json_array)-2):
            if json_array[i]['id_Q'] == id:
                if json_array[i]['mark'] != -1:
                    what_do = 1

    where_id = 0
    next_id = 0 
    previous_id = 0
    for test_id in range(0, len(questions_id)):
        if questions_id[test_id]['id_Q'] == id:
            where_id = test_id

    try:
        previous_id = questions_id[where_id - 1]['id_Q']
    except:
        previous_id = -1

    try:
        next_id = questions_id[where_id + 1]['id_Q']
    except:
        next_id = -1

    question = Question.objects.get(pk=id)
    question_1 = question.a_1
    question_2 = question.a_2
    question_3 = question.a_3
    question_4 = question.a_4
    context = {
        'name_question': question.q,
        'question_1': question_1,
        'question_2': question_2,
        'question_3': question_3,
        'question_4': question_4,
        'main_test_id': test_ques['id_T'],
        'id_question': id,
        'right': 0,
        'no_right': 0,
        'no_right_on': 0,
        'next_id': next_id,
        'previous_id': previous_id,
        'what_do': what_do
    }
    if request.method == "POST":
        right_answers = question.r_a
        answer = request.POST['question'] 
        if answer == right_answers:
            context['right'] = 1
            # Отправка данных на сервер с 
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
        connect = create_connection('C:/Users/Anastasiya/Documents/DiplomForWoman-main/Diplom/db.sqlite3')

        cursor = connect.cursor()
        your_select = f.read()
       # your_select = cursor.execute(your_select).fetchall()
       # teacher_select = cursor.execute(fromView).fetchall()        
        if your_select == fromView:
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


def deleteTask(request):
    teacher_lesson = Teacher_Lessons.objects.get(teacher_id = 1, lesson_id = 1)
    id_test = Teacher_Lessons_Test.objects.filter(id_TL = teacher_lesson.id)
    choise_ss = []
    for i in id_test:
        id_T = Test.objects.filter(pk= i.id_test).values('pk','title')
        choise_ss.append(id_T)

    choise = []
    for test in choise_ss:
        # print(test)
        choise.append({'id': int(test[0]['pk']), 'title': test[0]['title']})

    if request.method == "POST":
        what_test_delete = request.POST['delete']
        instance = Test.objects.get(id=what_test_delete)
        instance.delete()
        instance = Teacher_Lessons_Test.objects.get(id_test=what_test_delete)
        instance.delete()
        redirect("deleteTask")

    return render(request, 'appForDiplom/deleteTask.html', {'choise': choise})


def newTask(request):
    if request.method == "POST":
        new_test = Test(title=request.POST['newtask'])
        new_test.save()
        new_f = Teacher_Lessons_Test(
            id_test = new_test.id,
            id_TL = 1
        )
        new_f.save()
        # print()
        return redirect("/createTask")
    else:
        return render(request, 'appForDiplom/createTask.html')
    # new_test = Test(title=)
    # new_test.save()
    # redirect("createTask")