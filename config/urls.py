from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
]
# urls.py
from django.urls import path
from app.views import UsuarioLoginView

urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='login'),
]
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
from django.contrib import admin
from django.urls import path
from app.views import index  # substitua 'seu_app' pelo nome da sua app

urlpatterns = [
    path('', index, name='index'),  # ✅ página inicial
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
]
# urls.py
from django.urls import path
from app.views import UsuarioLoginView

urlpatterns = [
    path('', index, name='index'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
