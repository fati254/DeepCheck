from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

def home(request):
    return JsonResponse({"message": "Backend analyzer is working"})

##pour creation de compte (register)
from django.shortcuts import render, redirect
from .forms import RegisterForm
################pour register 
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

###########pour api de register

@api_view(['POST'])
def register_api(request):
    print("register api appelee ")

    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    
    if not  username or not password or not email :
        return Response({"status": "erreur"})
    if User.objects.filter(username=username).exists():
        return Response({"status": "exists"})
    if User.objects.filter(email=email).exists():
        return Response({"status": "email_exists"})
    User.objects.create_user(username=username, email=email , password=password)
        
    return Response({"status": "ook"})
    

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

######pour creer le dashboard 
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "analyzer/dashboard.html")


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect("login")


######pour la partie upload 
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

#######pour api de logiiiin 
@api_view(['POST'])
def login_api(request):
    print("login api appelee ")

    email = request.data.get("email")  
    password = request.data.get("password")

    try:
        user_obj = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"status": "error"})
    
    user = authenticate(username=user_obj.username, password=password)

    if user is not None:
        return Response({"status": "success"})
    else :
        return Response({"status": "error"})
    
#########pour scan less code de securite
from .security.scan import analyze_code

@api_view(['POST'])
def scan_api(request):
    code = request.data.get("code")

    if not code:
        return Response({"status": "error"})

    issues = analyze_code(code)
    score = max(0, 100 - len(issues) * 10)

    return Response({
        "status": "success",
        "issues": issues,
        "score": score
    })



from django.shortcuts import render

def editor_view(request):
    return render(request, "analyzer/editor.html")