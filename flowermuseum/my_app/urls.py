from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'), 
     path('about/', views.about, name='about'),
     path('flowers/', views.flower_index, name='flower-index'),
     path('Flowers/<int:flower_id>/', views.flower_detail, name='flower-detail'),
]
