from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import *


class PostForm(forms.Form):
    name = forms.URLField(label='Ссылка на статью')
    title = forms.CharField(max_length=255, label='Заголовок статьи')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст статьи')
    tag_list = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              label='Теги')
    likes = forms.IntegerField(label='Лайки', validators=[MinValueValidator(0), MaxValueValidator(10000)],
                               error_messages={'min_value': 'Число не может быть меньше, чем ноль!'},
                               widget=forms.NumberInput(attrs={'placeholder': '0'}))
