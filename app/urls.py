from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app'),
    path('machine/', views.machine, name='machine'),
    path('data/', views.get_data, name='get_data'),
    path('data-page/', views.data, name='data-page'),
    path('plc/', views.plc, name='data-page'),
    path('test/', views.test, name='data-page'),
]
