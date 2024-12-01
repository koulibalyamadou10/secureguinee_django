import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from tokenfirebase.models import TokenFirebase
from user.firebase.send_push import send_push_notification


# Create your views here.
@csrf_exempt
def update_token_firebase(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        token = data.get('token')

        print(f"{token}")

        if token:
            tk:TokenFirebase = TokenFirebase.objects.get(pk=1)
            tk.token = token
            tk.save()

            send_push_notification("title", "koulibaly amadou vas a l'ecole")

            return JsonResponse( {'code': 200, 'message': 'Action automatique crée avec succées' } )