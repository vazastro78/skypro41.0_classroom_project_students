from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from materials.models import Material


# Create your views here.

class MaterialListView(ListView):
    extra_context = {
        'title': 'Страница просмотра материалов'
    }
    template_name = 'materials/materials_list_all.html'


    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class MaterialCreateView(CreateView):
    model = Material
    fields = ( 'title', 'body',)
    template_name = 'materials/materials_create.html'

    def get_success_url(self):
        return reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()
        return super().form_valid(form)



class MaterialUpdateView(UpdateView):
    model = Material
    fields = ( 'title', 'body', 'is_published', )
    template_name = 'materials/materials_update_single.html'

    extra_context = {
        'title': 'Страница изменения отдельного материала'
    }
    def get_success_url(self):
        return reverse_lazy('materials:view_single',args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()
        return super().form_valid(form)


class MaterialDetailView(DetailView):
    model = Material
    extra_context = {
        'title': 'Страница просмотра отдельного материала'
    }
    template_name = 'materials/materials_view_single.html'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class MaterialDeleteView(DeleteView):
    model = Material
    extra_context = {
        'title': 'Страница удаления отдельного материала'
    }
    template_name = 'materials/materials_confirm_delete_single.html'
    def get_success_url(self):
        return reverse_lazy('materials:list')

