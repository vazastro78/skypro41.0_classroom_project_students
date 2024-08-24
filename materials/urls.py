from django.urls import path


from materials.apps import MaterialsConfig
from materials.models import Material
from materials.views import MaterialListView, MaterialCreateView, MaterialDetailView

app_name = MaterialsConfig.name



urlpatterns = [
    path("", MaterialListView.as_view(), name='list'),
    path("create/", MaterialCreateView.as_view() , name='create'),
    path("view/<int:pk>/", MaterialDetailView.as_view(), name='view_single'),

]
