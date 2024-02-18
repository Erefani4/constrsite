from django.shortcuts import render, redirect
from .models import Shed
from .forms import ShedForm


def katalog_home(request):
    katalog = Shed.objects.all()
    return render(request, 'katalog/katalog_home.html', {'katalog': katalog})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ShedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/katalog')
        else:
            error = 'Форма была неверной'

    form = ShedForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'katalog/create.html', data)