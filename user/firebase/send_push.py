import os
import secureguinee.settings as set
import firebase_admin
from firebase_admin import credentials, messaging
from tokenfirebase.models import TokenFirebase

cred = credentials.Certificate(os.path.join(set.BASE_DIR, 'serviceAccountKey.json' ) )
print(f"*****************{set.BASE_DIR}")
firebase_admin.initialize_app(cred)

def send_push_notification(title, msg, dataObject=None):
    tken:TokenFirebase = TokenFirebase.objects.get(pk=1)
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        token=tken.token,
    )

    try:
        response = messaging.send(message)
        print("Successfully sent message:", response)
    except Exception as e:
        print(e)
        print("Error sending message:", e)