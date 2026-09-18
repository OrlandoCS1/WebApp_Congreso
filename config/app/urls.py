from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('evaluador/', views.evaluador, name='evaluador'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('form_usuarios/', views.form_usuarios, name='form_usuarios')
]


