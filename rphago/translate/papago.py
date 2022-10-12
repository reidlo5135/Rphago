import os
import json
import urllib.request, urllib.parse
from django.core.exceptions import ImproperlyConfigured

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


def get_common_response(data, url):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        print('restRequest response : ', response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)