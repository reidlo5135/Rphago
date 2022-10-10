from django.urls import path
from . import views

app_name = 'translate'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:language>/', views.lang, name='lang')
]
