import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from autorite.models import Autorite
from autorite.serializers import AutoriteSerializer


# Create your views here.
@csrf_exempt
def autorite(request):
    if request.method == 'POST':
        try:
            # Charger les données JSON de la requête
            data = json.loads(request.body)

            # Filtrer les utilisateurs par l'ID fourni
            autorites = Autorite.objects.filter(id=data.get('id'))

            # Vérifier si un utilisateur existe
            if autorites.exists():
                autorite = autorites.first()
                serialized_user = AutoriteSerializer(autorite)
                return JsonResponse(serialized_user.data, safe=False)
            else:
                return JsonResponse({"data": "aucune autorité correspondante"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)

    return JsonResponse({"data": "erreur de méthode"}, status=405)

@csrf_exempt
def autorites(request):
    if request.method == 'GET':

        # Filtrer les utilisateurs par l'ID fourni
        autorites = Autorite.objects.all()

        print(autorites)

        serialized_user = AutoriteSerializer(autorites, many=True)
        return JsonResponse(serialized_user.data, safe=False, status=200)

    return JsonResponse({"data": "erreur de méthode"}, status=405)

@csrf_exempt
def add_autorite(request):
    if request.method == 'POST':
        try:
            # Charger les données JSON de la requête
            data = json.loads(request.body)

            print(f"data {data}")

            email = data.get('email')
            password = data.get('password')


            autorite = Autorite(email=email, password=password)
            autorite.save()

            autorite_serializer = AutoriteSerializer(autorite)
            return JsonResponse(autorite_serializer.data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)
    return JsonResponse({"data": "erreur de méthode"}, status=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')

        autorites = Autorite.objects.filter(email=email).values() | Autorite.objects.filter(password=password).values()
        if autorites.exists():
            autorite = autorites.first()
            autorite_serializer = AutoriteSerializer(autorite)
            return JsonResponse(autorite_serializer.data, status=200)
        return JsonResponse({"data":"Identifiant de connexion incorrect"}, status=404)
    return JsonResponse({"data":"methode incorrect !"}, status=404)

