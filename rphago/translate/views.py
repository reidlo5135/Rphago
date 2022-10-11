import os
import json
import requests
import urllib.request, urllib.parse
from django.shortcuts import render
from pprint import pprint
from django.core.exceptions import ImproperlyConfigured
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

SECRET_FILES = os.path.join(r'C:\Rphago\SecretKey.json')

with open(SECRET_FILES, 'r') as f:
    secrets = json.loads(f.read())


def get_secret(settings, secrets=secrets):
    try:
        return secrets[settings]
    except KeyError:
        error_msg = "Set the {} environment variable".format(settings)
        raise ImproperlyConfigured(error_msg)


client_id = get_secret('CLIENT_ID')
client_secret = get_secret('CLIENT_SECRET')


def index(request):
    return render(request, 'translate/index.html')


def lang(request, language):
    context = {'lang': language}
    return render(request, 'translate/index.html', context)


@csrf_exempt
def get_translate(request):
    global jsonObject
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        print(jsonObject)

    encText = urllib.parse.quote(jsonObject.get('text'))
    data = "source=ko&target=" + "en" + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
