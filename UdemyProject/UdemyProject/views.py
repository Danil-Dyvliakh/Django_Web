from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    a = "Новая страница1"
    text_index = "Something index text"
    return render(request, './index.html',{
        'a': a,
        'text': text_index
    })
