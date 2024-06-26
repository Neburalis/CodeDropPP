from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse

import CodeDrop
from .models import CodeDropDB
from .forms import CodeDropForm


# Create your views here.

def create(request):
    error = ''
    if request.method == 'POST':
        form = CodeDropForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect('view_code', unique_id=entry.unique_id)

    form = CodeDropForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'code_drop/create.html', data)


def view_code(request, unique_id):
    code_data = get_object_or_404(CodeDropDB, unique_id=unique_id)

    unique_url = request.build_absolute_uri(reverse('view_code', args=[unique_id]))

    data = {
        'code_data': code_data,
        'unique_url': unique_url,
    }

    return render(request, 'code_drop/view.html', data)


class Index(CreateView):
    model = CodeDropDB
    form_class = CodeDropForm
    # context_object_name = 'form'
    # fields = ['name', 'text']

    template_name = 'code_drop/create.html'
    success_url = '/'
