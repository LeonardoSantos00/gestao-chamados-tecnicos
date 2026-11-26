from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.http import require_POST

from ..forms.forms_planos import PlanoForm
from ..models import Plano


def ver_planos(request):
    planos = Plano.objects.all()
    return render(request, "planos.html", {"planos": planos})

def detalhar_plano(request, id):
    plano = get_object_or_404(Plano, pk=id)
    return render(request, "detalhar_plano.html", {"plano": plano})