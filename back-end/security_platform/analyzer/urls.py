
## Ici tu mets toutes tes pages (views) 
from django.urls import path
from . import views
from .views import login_api
from .views import register_api
from .views import scan_api
from .views import editor_view 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("upload/", views.upload_code, name="upload"),
    path('api/login/', login_api),
    path('api/register/', register_api),
    path('api/scan/', scan_api),
    path('editor/', editor_view, name='editor'),
]
