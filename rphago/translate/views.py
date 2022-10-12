import json
import urllib.request, urllib.parse
from . import papago
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return render(request, 'translate/index.html')


@csrf_exempt
def get_translate(request):
    global jsonObject
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        print(jsonObject)

    encText = urllib.parse.quote(jsonObject.get('text'))
    code_source = get_source_code(jsonObject.get('text'))
    code_target = get_target_code(jsonObject.get('lang'))
    print('source_code : ', code_source)
    print('target_code : ', code_target)
    data = "source=" + code_source + "&target=" + code_target + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    response = json.loads(papago.get_common_response(data, url)).get("message").get("result")
    print('get_translate response : ', response)
    result = {
        "tarLangType": response.get("tarLangType"),
        "translatedText": response.get("translatedText")
    }

    return JsonResponse(result)


def get_source_code(text):
    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    response = papago.get_common_response(data, url)
    print('get_source_code response : ', response)

    return json.loads(response).get("langCode")


def get_target_code(lang):
    global code
    if lang == "한국어":
        code = "ko"
    elif lang == "일본어":
        code = "ja"
    elif lang == "중국어(간체)":
        code = "zh-CN"
    elif lang == "중국어(번체)":
        code = "zh-TW"
    elif lang == "힌디어":
        code = "hi"
    elif lang == "영어":
        code = "en"
    elif lang == "스페인어":
        code = "es"
    elif lang == "프랑스어":
        code = "fr"
    elif lang == "독일어":
        code = "de"
    elif lang == "포르투갈어":
        code = "pt"
    elif lang == "베트남어":
        code = "vi"
    elif lang == "인도네시아어":
        code = "id"
    elif lang == "페르시아어":
        code = "fa"
    elif lang == "아랍어":
        code = "ar"
    elif lang == "미얀마어":
        code = "mm"
    elif lang == "태국어":
        code = "th"
    elif lang == "러시아어":
        code = "ru"
    elif lang == "이탈리아어":
        code = "it"
    else:
        code = "unk"

    return code
