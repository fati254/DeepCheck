from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return JsonResponse({"message": "Backend analyzer is working"})

# Create your views here.
##pour creation de compte (register)
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
####
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # 🔥 crée le compte correctement
            return redirect("login")
        else:
            print(form.errors)  # 🔍 voir erreurs
    else:
        form = RegisterForm()

    return render(request, "analyzer/register.html", {"form": form})

##pour login a votre compte 
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")

    return render(request, "analyzer/login.html")

##pour creer le dashboard 
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "analyzer/dashboard.html")

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect("login")


##pour la partie upload 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def upload_code(request):
    if request.method == "POST":
        code_file = request.FILES.get("file")

        if code_file:
            content = code_file.read().decode("utf-8")

            # temporaire : afficher contenu
            return render(request, "analyzer/result.html", {
                "code": content
            })

    return render(request, "analyzer/upload.html")

###pour api de logiiiin 
@api_view(['POST'])
def login_api(request):
    email = request.data.get("email")
    password = request.data.get("password")

    #test simple ( pour ameliorer ensuite )
    if email == "test@gmail.com" and password == "123":
        return Response({"status": "success"})
    else :
        return Response({"status": "error"})