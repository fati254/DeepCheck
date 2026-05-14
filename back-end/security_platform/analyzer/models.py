from django.db import models

# Create your models here.
###Sauvegarder le code envoyé par l’utilisateur

from django.db import models
from django.contrib.auth.models import User

class CodeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ScanHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    language = models.CharField(max_length=50)

    score = models.IntegerField()

    total_issues = models.IntegerField(default=0)

    critical_issues = models.IntegerField(default=0)

    code = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.language}"