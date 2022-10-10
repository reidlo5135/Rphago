from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


class IndexView:
    template_name = "translateApp/index.html"


def index(request):
    template = loader.get_template(IndexView.template_name)
    return HttpResponse(template.render())


def lang(request, language):
    context = {'lang': language}
    return render(request, 'translateApp/index.html', context)
