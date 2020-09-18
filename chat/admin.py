from django.contrib import admin
from .models import Contact, Chat, Message, ChatNew, MessageNew

admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(MessageNew)
admin.site.register(ChatNew)