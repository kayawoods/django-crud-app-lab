from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Flower




def flower_index(request): 
     flowers = Flower.objects.all()
     return render(request, 'flowers/index.html', {'flowers': flowers})

def home(request): 
    return render(request,'home.html')

def about(request):
     return render(request, 'about.html')

def flower_detail(request, flower_id):
     flower = Flower.objects.get(id=flower_id)
     return render(request, 'flowers/details.html', {'flower': flower})

class FlowerCreate(CreateView):
     model = Flower 
     fields = '__all__' 

class FlowerUpdate(UpdateView): 
     model = Flower 
     fields = ['type', 'scent', 'description', 'image']

class FlowerDelete(DeleteView): 
     model = Flower 
     success_url = '/flowers/'