from django.urls import path, include
from . import views as chat

urlpatterns = [
    path('test/', chat.test.as_view()),
    path('', chat.index, name='index'),
    path('<str:room_name>/', chat.room, name='room'),
]