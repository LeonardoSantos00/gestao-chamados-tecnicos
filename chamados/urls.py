from django.urls import path
from . import views



# Urls de planos

urlpatterns = [
    path('planos/', views.ver_planos, name='planos'),
]
