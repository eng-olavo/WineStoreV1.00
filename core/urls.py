from django.urls import path

from .views import IndexView, CreateVinhoView, UpdateVinhoView, DeleteVinhoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateVinhoView.as_view(), name='add_vinho'),
    path('<int:pk>/update/', UpdateVinhoView.as_view(), name='upd_vinho'),
    path('<int:pk>/delete/', DeleteVinhoView.as_view(), name='del_vinho'),
]
