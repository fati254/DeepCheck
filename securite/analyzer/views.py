from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Backend analyzer is working"})

# Create your views here.
# hadchi lizdt 

from .utils import analyze_code  # On importe notre fonction depuis utils.py

def analyze_view(request):
    # On récupère le code envoyé dans la requête (GET)
    code = request.GET.get("code", "")  # Si aucun code fourni, on prend une chaîne vide

    # On analyse le code avec notre fonction
    issues = analyze_code(code)

    # On retourne le résultat sous format JSON
    return JsonResponse({"issues": issues})