from django.urls import path
from .views import views_planos

app_name = 'chamados'

urlpatterns = [
    path('planos/', views_planos.ver_planos, name='planos'),
]
