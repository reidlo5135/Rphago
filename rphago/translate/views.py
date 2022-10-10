from django.shortcuts import render


def index(request):
    return render(request, 'translate/index.html')


def lang(request, language):
    context = {'lang': language}
    return render(request, 'translate/index.html', context)
