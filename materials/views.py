from django.views.generic import CreateView, ListView, DetailView, DeleteView

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



class MaterialDetailView(DetailView):
    model = Material
    extra_context = {
        'title': 'Страница просмотра отдельного материала'
    }
    template_name = 'materials/materials_view_single.html'

class MaterialDeleteView(DeleteView):
    model = Material
    extra_context = {
        'title': 'Страница удаления отдельного материала'
    }
    template_name = 'materials/materials_confirm_delete_single.html'
    def get_success_url(self):
        return reverse_lazy('materials:list')

