from django.shortcuts import render
from .models import Shed

def katalog_home(request):
    katalog = Shed.objects.all()
    return render(request, 'katalog/katalog_home.html', {'katalog': katalog})