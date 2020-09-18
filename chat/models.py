from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class MessageNew(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


class ChatNew(models.Model):
	room_id = models.IntegerField(null=True, blank=True)
	is_group = models.BooleanField(default=False)
	user_list = models.ManyToManyField(User, related_name='users', blank=True)
	messages = models.ManyToManyField(MessageNew, blank=True)

	def __str__(self):
		return "{}".format(self.room_id)


class Contact(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)
