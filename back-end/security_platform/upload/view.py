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