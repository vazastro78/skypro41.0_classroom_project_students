
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy, reverse

from materials.models import Material


# Create your views here.

class MaterialListView(ListView):
    extra_context = {
        'title': 'Страница просмотра материалов'
    }
    template_name = 'materials/materials_list_all.html'


    model = Material

class MaterialCreateView(CreateView):
    model = Material
    fields = ( 'title', 'body',)
    template_name = 'materials/materials_create.html'

    def get_success_url(self):
        return reverse_lazy('materials:list')



