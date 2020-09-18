from django.urls import path, include
from . import views as chat

urlpatterns = [
    path('', chat.ChatListView.as_view(), name='chat_list'),
    path('self/', chat.UserChatList.as_view(), name='user_chat_list'),
    
]