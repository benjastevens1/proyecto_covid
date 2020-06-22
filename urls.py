from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('registro', views.registro, name="registro"),
    path('estadistica', views.estadistica, name='estadistica'),
]
