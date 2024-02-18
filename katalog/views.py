from django.shortcuts import render, redirect
from .models import Shed
from .forms import ShedForm
from django.views.generic import UpdateView, DeleteView


def katalog_home(request):
    katalog = Shed.objects.all()
    return render(request, 'katalog/katalog_home.html', {'katalog': katalog})


class KatalogUpdateView(UpdateView):
    model = Shed
    template_name = 'katalog/create.html'

    form_class = ShedForm


class KatalogDeleteView(DeleteView):
    model = Shed
    success_url = '/katalog/'
    template_name = 'katalog/katalog-delete.html'




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