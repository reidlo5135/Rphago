from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("TEST INDEX")


def lang(request, language):
    context = {'lang': language}
    return render(request, 'translate/index.html', context)
