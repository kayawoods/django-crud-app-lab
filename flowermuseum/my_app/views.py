from django.shortcuts import render


class Flower: 
     def __init__(self, chosen_name, type, scent, description):
          self.chosen_name = chosen_name 
          self.type = type
          self.scent = scent 
          self.description = description 
flowers = [ 
     Flower('Marcus', 'Sunflower', 'Floral Butter', 'lush'), 
     Flower('Hannah', 'Rose', 'Romance', 'thorny'),
     Flower('Lila', 'Daisy', 'Skunk', 'vibrant af')
]

def flower_index(request): 
     return render(request, 'flowers/index.html', {'flowers': flowers})

def home(request): 
    return render(request,'home.html')

def about(request):
     return render(request, 'about.html')