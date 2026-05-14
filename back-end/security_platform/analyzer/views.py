from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .security.scan import analyze_code
from .models import ScanHistory
from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt
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

    scans = ScanHistory.objects.filter(
        user=request.user
    ).order_by("-created_at")

    total_scans = scans.count()

    critical_issues = sum(
        scan.critical_issues for scan in scans
    )

    average_score = scans.aggregate(
        Avg("score")
    )["score__avg"] or 0

    context = {
        "total_scans": total_scans,
        "critical_issues": critical_issues,
        "average_score": round(average_score),
        "recent_scans": scans[:5]
    }

    return render(
        request,
        "analyzer/dashboard.html",
        context
    )
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


@api_view(['POST'])
def scan_api(request):
    code = request.data.get("code")
    language = request.data.get("language", "Python")
    

    data = request.data
    filename = data.get("filename","unknown.py")

    if not code:
        return Response({"status": "error"})

    issues = analyze_code(code, language)
    score = max(0, 100 - len(issues) * 10)

    critical_count = sum(
    1 for issue in issues
    if "critical" in issue.get(
        "severity",
        ""
    ).lower()
)
# =========================
# SAVE SCAN
# =========================

    ScanHistory.objects.create(

         user=User.objects.first(),

         filename=filename,

         language=language,

         total_issues=len(issues),

         critical_issues=critical_count,

         score=score,

         code=code

        )


    return Response({
        "status": "success",
        "issues": issues,
        "score": score
       })





def editor_view(request):
    return render(request, "analyzer/editor.html")


def dashboard_api(request):

    scans = ScanHistory.objects.all().order_by("-created_at")

    total_scans = scans.count()

    critical_issues = sum(
        scan.critical_issues for scan in scans
    )

    average_score = scans.aggregate(
        Avg("score")
    )["score__avg"] or 0

    recent_scans = []

    for scan in scans[:5]:

        recent_scans.append({
            "filename": scan.filename, 
            "score": scan.score,
            "issues": scan.total_issues,
            "date": scan.created_at.strftime("%Y-%m-%d %H:%M"),
        })

    return JsonResponse({
        "total_scans": total_scans,
        "critical_issues": critical_issues,
        "average_score": round(average_score),
        "recent_scans": recent_scans
    })

def history_page(request):

    scans = ScanHistory.objects.order_by(
        "-created_at"
    )

    return render(

        request,

        "analyzer/history.html",

        {
            "scans": scans
        }

    )