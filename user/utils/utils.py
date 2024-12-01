from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_message_to_chat(message:str):
    print("started")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "chat_room",
        {
            "type": "chat_message",
            "message": message
        }
    )
    print("sended")