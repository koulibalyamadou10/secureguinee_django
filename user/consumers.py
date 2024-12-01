# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None

    def connect(self):
        self.room_name = 'chat_room'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def receive(self, text_data):
        # from user.models import SCUser
        print(f"data received from websocket {text_data}")

        data = json.loads(text_data)
        if data['page']:
            if data['page'] == 'contact':
                from message.models import Message
                from message.serializers import MessageSerializer
                from autorite.models import Autorite
                from user.models import SCUser
                from user.utils.utils import send_message_to_chat
                if data['init'] != 1:

                    u = data['user']
                    sender = SCUser.objects.filter(pk=u['id']).first()

                    authorities = Autorite.objects.all()
                    for authority in authorities:
                        Message.objects.create(
                            sender=sender,
                            recipient=authority,
                            message=data['message']
                        )

                    messages = Message.objects.filter(sender=sender)
                    serializer = MessageSerializer(messages, many=True)
                    send_message_to_chat(message=serializer.data)
                else:
                    u = data['user']
                    sender = SCUser.objects.filter(pk=u['id']).first()
                    messages = Message.objects.filter(sender=sender)
                    serializer = MessageSerializer(messages, many=True)

                    print(serializer.data)
                    print(type(serializer.data))
                    send_message_to_chat(message=serializer.data)

        # id = data['user']['id']
        # message = data['message']
        #
        # scusers = SCUser.objects.filter(pk=id).values()
        # print(scusers.first())

        

    # Méthode appelée pour envoyer un message au groupe
    def chat_message(self, event):
        message = event['message']

        # Envoie le message à WebSocket
        self.send(text_data=json.dumps({
            'data': message
        }))