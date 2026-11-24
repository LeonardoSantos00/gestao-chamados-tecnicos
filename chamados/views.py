from django.shortcuts import render

# Create your views here.



# Views de planos

def ver_planos(request):
    return render(request, "planos.html")