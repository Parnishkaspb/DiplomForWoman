from django import forms
from .models import Videos, Practice, User_Test

class VideoForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        "id": 'comment',
        "name": 'comment',
        "class": 'form-control form-control-sm',
    }))
    file = forms.CharField( required=True, label='Ссылка на видео', widget=forms.Textarea(attrs={
        "id": 'file',
        "class": 'form-control',
        "placeholder": 'Вставьте html-код видео'
    }))
    
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ['title', 'content', 'number', 'practice']
        widgets = {
            'title': forms.TextInput(attrs={
                "id": 'comment',
                "name": 'comment',
                'class': 'form-control'
                }),
            'content': forms.Textarea(attrs={
                "id": 'content',
                "name": 'comment',
                'class': 'form-control'
                }),
            'number': forms.NumberInput(attrs={
                'id': 'number',
                'min': 5,
                'max': 10,
                'class': 'form-control'
                })
        }

class DoPracticeForm(forms.Form):
    do = forms.CharField(label='Поле для практики', widget=forms.Textarea(attrs={
        "id": 'do',
        "class": 'form-control',
        'required': True,
        'rows': 25, 
        'cols': 10,
    }))

class TaskForm(forms.Form):
    title = forms.CharField( required=True, label='Вопрос', widget=forms.TextInput(attrs={
        "id": 'title',
        "class": 'form-control',
        "placeholder": 'Введите вопрос'
    }))
    answer_1 = forms.CharField( required=True, label='1 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_1',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_2 = forms.CharField( required=True, label='2 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_2',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_3 = forms.CharField( required=True, label='3 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_3',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    answer_4 = forms.CharField( required=True, label='4 ответ', widget=forms.TextInput(attrs={
        "id": 'answer_4',
        "class": 'form-control',
        "placeholder": 'Введите ответ'
    }))
    correct_answer = forms.CharField( required=True, label='Правильный ответ', widget=forms.TextInput(attrs={
        "id": 'correct_answer',
        "class": 'form-control',
        "placeholder": 'Введите правильный ответ'
    }))
    what_theme = forms.CharField(widget=forms.NumberInput(attrs={
        "id": 'what_theme',
        'type': 'hidden'
    }))




class UserTestForm(forms.ModelForm):
    class Meta:
        model = User_Test
        fields = ['json_massive']
        widgets = {
            'json_massive': forms.Textarea(attrs={
                "id": 'json_massive',
                }),
        }