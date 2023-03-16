from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
    # cookie = HttpResponse('<h4>Проверка!</h4>')
    # cookie.set_cookie('personal_id', 123)
    # return cookie

# def index(request):
#     show = request.COOKIES['personal_id']
#     return HttpResponse(f'<h4>Проверка! На куках: {show}</h4>')

# def index(request):
#     json_string = {
#         "text":"<h1> Добро пожаловать </h1>", 
#         "task": [
#             {
#                 'number': '1',
#                 'q':'Когда был основан ГУАП?',
#                 'var': [ '2222', '2221', '2223', '2224'],
#                 'answer': '2223'
#             }, 
#             {
#                 'number': '2',
#                 'q':'Когда был основан Питер?',
#                 'var': [ '1703', '1702', '1700', '1701'],
#                 'answer': '1703'
#             }, 
#         ]
#     }
#     return render(request, 'appForDiplom/lab.html', {'json_string': json_string})

def index(request):
    json_string = {
        "text":"<h1> Добро пожаловать </h1>", 
        "task": [
            {
                'number': '1',
                'q':'Создать таблицу под названием <strong>DB</strong> следующей структуры: <table border="1" cellpadding="1" cellspacing="1"><tr><td>Поле</td><td>Тип, описание</td></tr><tr><td><strong>ID</strong></td><td>INT PRIMARY KEY AUTO_INCREMENT</td></tr></table>'
            }
        ]
    }
    
    return render(request, 'appForDiplom/prac.html', {'json_string': json_string})