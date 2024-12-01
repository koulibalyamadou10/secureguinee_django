import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from autorite.models import Autorite
from message.models import Message
from message.serializers import MessageSerializer
from user.models import SCUser
from user.serializers import SCUserSerializer

# Create your views here.
@csrf_exempt
def test(request):
    messages = Message.objects.filter(sender_id=1)
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        # Vérifiez si un fichier a été envoyé
        if 'image' not in request.FILES:
            return JsonResponse({"error": "No file provided"}, status=400)

        file = request.FILES['image']

        sender = SCUser.objects.filter(pk=int(request.POST.get('id'))).first()
        authorities = Autorite.objects.all()
        for authority in authorities:
            Message.objects.create(
                sender=sender,
                recipient=authority,
                image=file
            )


        # Retournez l'URL de l'image sauvegardée
        return JsonResponse({"succes": "image saved"}, status=201)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def user(request):
    if request.method == 'POST':
        try:
            # Charger les données JSON de la requête
            data = json.loads(request.body)

            # Filtrer les utilisateurs par l'ID fourni
            sgusers = SCUser.objects.filter(id=data.get('id'))

            # Vérifier si un utilisateur existe
            if sgusers.exists():
                sguser = sgusers.first()
                serialized_user = SCUserSerializer(sguser)
                return JsonResponse(serialized_user.data, safe=False)
            else:
                return JsonResponse({"data": "aucun utilisateur correspondant"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)

    return JsonResponse({"data": "erreur de méthode"}, status=405)

@csrf_exempt
def users(request):
    if request.method == 'GET':

        # Filtrer les utilisateurs par l'ID fourni
        sgusers = SCUser.objects.all()

        print(sgusers)

        serialized_user = SCUserSerializer(sgusers, many=True)
        return JsonResponse(serialized_user.data, safe=False, status=200)

    return JsonResponse({"data": "erreur de méthode"}, status=405)

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        try:
            # Charger les données JSON de la requête
            data = json.loads(request.body)

            print(f"data {data}")

            nom = data.get('nom')
            prenom = data.get('prenom')
            numero = data.get('numero')
            password = data.get('password')

            print(f"{nom} {prenom} {numero} {password}")

            scuser = SCUser(nom=nom, prenom=prenom, numero=numero, password=password)
            scuser.save()

            scurer_serializer = SCUserSerializer(scuser)
            return JsonResponse(scurer_serializer.data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)
    return JsonResponse({"data": "erreur de méthode"}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        numero = data.get('numero')
        password = data.get('password')

        users = SCUser.objects.filter(numero=numero).values() | SCUser.objects.filter(password=password).values()
        if users.exists():
            user = users.first()
            s_serialier = SCUserSerializer(user)
            return JsonResponse(s_serialier.data, status=200)
        return JsonResponse({"data":"Identifiant de connexion incorrect"}, status=404)
    return JsonResponse({"data":"methode incorrect !"}, status=404)
