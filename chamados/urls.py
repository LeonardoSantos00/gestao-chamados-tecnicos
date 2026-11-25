from django.urls import path
from .views import (
    views_planos,
    views_clientes,
    views_equipamentos,
    views_tecnicos,
    views_chamados,
)

app_name = 'chamados'

urlpattenrs = [

    # Dashboard / Home
    # path ('', views_chamados.home, name='home'),

    #Foi solicitado: a criação, leitura/listagem, atualização, exclusão (CRUD) e uma visão de detalhamento (detail view)
    # Pra padronizar e facilitar já adiantei um, o list, dos 5 módulos, so descomentar

    # Módulo 1: Planos
    # path('planos/', views_planos.plano_list, name='plano_list'),

    # Módulo 2: Clientes
    # path('clientes/', views_clientes.cliente_list, name='cliente_list'),

    # Módulo 3: Equipamentos
    # path('equipamentos/', views_equipamentos.equipamento_list, name='equipamento_list'),

    # Módulo 4: Tecnicos
    # path('tecnicos/', views_tecnicos.tecnico_list, name='tecnico_list'),

    # Módulo 5: Chamados
    # path('chamados/', views_chamados.chamado_list, name='chamado_list'),

]