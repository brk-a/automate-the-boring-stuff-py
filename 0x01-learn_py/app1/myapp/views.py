from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    context = {
        'name': 'FNjakai',
        'city': 'Nairobi',
        }
    return render(req, 'index.html', context)


def counter(req):
    text = req.GET['text']
    word_count = len(text.split())
    context = {
        'word_count': word_count,
    }
    return render(req, 'counter.html', context)
