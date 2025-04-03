from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Flower
from .forms import WateringForm




def flower_index(request): 
     flowers = Flower.objects.all()
     return render(request, 'flowers/index.html', {'flowers': flowers})

def home(request): 
     return render(request,'home.html')

def about(request):
     return render(request, 'about.html')

def flower_detail(request, flower_id):
     flower = Flower.objects.get(id=flower_id)
     watering_form = WateringForm() 
     return render(request, 'flowers/details.html', {'flower': flower, 'watering_form' : watering_form})

class FlowerCreate(CreateView):
     model = Flower 
     fields = '__all__' 

class FlowerUpdate(UpdateView): 
     model = Flower 
     fields = ['type', 'scent', 'description', 'image']

class FlowerDelete(DeleteView): 
     model = Flower 
     success_url = '/flowers/'

def add_watering(request, flower_id): 
     form = WateringForm(request.POST)
     if form.is_valid(): 
          new_watering = form.save(commit=False)
          new_watering.flower_id = flower_id 
          new_watering.save() 
     return redirect('flower-detail', flower_id=flower_id)
