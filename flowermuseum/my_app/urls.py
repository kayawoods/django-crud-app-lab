from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'), 
     path('about/', views.about, name='about'),
     path('flowers/', views.flower_index, name='flower-index'),
     path('Flowers/<int:flower_id>/', views.flower_detail, name='flower-detail'),
     path('flowers/create/', views.FlowerCreate.as_view(), name='flower-create'),
     path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flower-update'),
     path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flower-delete'),
     path('flowers/<int:flower_id>/add-watering/', views.add_watering, name='add-watering'),
]
