from django.shortcuts import render


def ver_planos(request):
    return render(request, "planos.html")