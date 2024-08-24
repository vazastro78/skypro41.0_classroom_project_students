from django.urls import path


from materials.apps import MaterialsConfig
from materials.models import Material
from materials.views import MaterialListView, MaterialCreateView, MaterialDetailView, MaterialDeleteView, \
    MaterialUpdateView

app_name = MaterialsConfig.name



urlpatterns = [
    path("", MaterialListView.as_view(), name='list'),
    path("create/", MaterialCreateView.as_view() , name='create'),
    path("update/<int:pk>/", MaterialUpdateView.as_view(), name='update_single'),
    path("view/<int:pk>/", MaterialDetailView.as_view(), name='view_single'),
    path("detele/<int:pk>/", MaterialDeleteView.as_view(), name='delete_single'),

]
