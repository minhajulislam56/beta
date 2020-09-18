from rest_framework.views import APIView
from rest_framework.response import Response
from chat.models import Chat, Contact, ChatNew
from . import serializers as chat_slr
class ChatListView(APIView):
	def get(self, request, *args, **kwargs):
		username = self.request.query_params.get('username', None)
		contact = Contact.objects.filter(user__username=username).first()
		qs = contact.chats.all()
		slr = chat_slr.ChatSerializer(qs, many=True)
		return Response(slr.data)

class UserChatList(APIView):

	def get(self, request, *args, **kwargs):
		user = self.request.user
		qs = ChatNew.objects.filter(user_list__in=[user])
		data = [{
			'room_id': data.room_id,
			'is_group': data.is_group,
			'contact': [contact.id for contact in data.user_list.all().exclude(id=user.pk)],
			'messages': [{
				'content': message.content,
				'time': message.timestamp
			} for message in data.messages.all().order_by('-timestamp')]
		}for data in qs]
		return Response(data, 200)