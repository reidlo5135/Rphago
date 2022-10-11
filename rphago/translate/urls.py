from django.urls import path
from . import views

app_name = 'translate'
urlpatterns = [
    path('', views.index, name='index'),
    path('translate/', views.get_translate, name='index'),
    path('<str:language>/', views.lang, name='lang'),
    path('<str:language>/', views.get_translate, name='lang')
]
