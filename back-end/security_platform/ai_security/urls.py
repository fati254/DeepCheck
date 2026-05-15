from django.urls import path
from . import views

urlpatterns = [
    path('', views.assistant, name='assistant'),
    path('api/',views.assistant_api,name='assistant_api'),
]