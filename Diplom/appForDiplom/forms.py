from django import forms
from .models import Videos

class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'content', 'video']
        widgets = {
            'title': forms.TextInput(attrs={ 
                "id": 'title',
                "class": 'form-control',
                'required': True,
                "placeholder": 'Введите наименование задания'
            }),
            'content': forms.Textarea(attrs={ 
                "id": 'content',
                "class": 'form-control',
                "placeholder": 'Введите дополнительный материал'
            }),
            # 'video': forms.FileField(),
        }

class TaskForm(forms.Form):
    title = forms.CharField(max_length=30, required=True, label='Вопрос', widget=forms.TextInput(attrs={
        "id": 'title',
        "class": 'form-control',
        "placeholder": 'Введите вопрос'
    }))
    answer_1 = forms.CharField(max_length=50, required=True, label='1 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_1',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_2 = forms.CharField(max_length=50, required=True, label='2 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_2',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_3 = forms.CharField(max_length=50, required=True, label='3 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_3',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_4 = forms.CharField(max_length=50, required=True, label='4 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_4',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    correct_answer = forms.CharField(max_length=50, required=True, label='Правильный ответ', widget=forms.TextInput(attrs={
        "id": 'correct_answer',
        "class": 'form-control',
        "placeholder": 'Введите правильный ответ'
    }))