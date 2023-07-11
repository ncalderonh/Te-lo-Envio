from django.urls import path
from . import views
from .views import RegisterView, ProductorRegisterView, ProductorLoginView, UsuarioLoginView

urlpatterns = [
    path('', views.index, name='principal'),
    path('productor', views.indexPro, name='productor'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_productor/', ProductorRegisterView.as_view(), name='registerproductor'),
    path('login_productor/', ProductorLoginView.as_view(), name='productor_login'),
]