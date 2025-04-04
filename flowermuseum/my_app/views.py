from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth import login
from .models import Flower
from .forms import WateringForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




@login_required
def flower_index(request): 
     flowers = Flower.objects.filter(user=request.user)
     return render(request, 'flowers/index.html', {'flowers': flowers})

class Home(LoginView):
     template_name = 'home.html'


def about(request):
     return render(request, 'about.html')

@login_required
def flower_detail(request, flower_id):
     flower = Flower.objects.get(id=flower_id)
     watering_form = WateringForm() 
     return render(request, 'flowers/details.html', {'flower': flower, 'watering_form' : watering_form})

class FlowerCreate(LoginRequiredMixin, CreateView):
     model = Flower 
     fields = ['chosen_name', 'type', 'scent', 'description', 'image'] 

     def form_valid(self, form):
          form.instance.user = self.request.user  
          return super().form_valid(form)

class FlowerUpdate(LoginRequiredMixin, UpdateView): 
     model = Flower 
     fields = ['type', 'scent', 'description', 'image']

class FlowerDelete(LoginRequiredMixin, DeleteView): 
     model = Flower 
     success_url = '/flowers/'

@login_required
def add_watering(request, flower_id): 
     form = WateringForm(request.POST)
     if form.is_valid(): 
          new_watering = form.save(commit=False)
          new_watering.flower_id = flower_id 
          new_watering.save() 
     return redirect('flower-detail', flower_id=flower_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flower-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   

  