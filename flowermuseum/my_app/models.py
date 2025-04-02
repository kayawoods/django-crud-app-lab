from django.db import models
from django.urls import reverse

class Flower(models.Model):
    chosen_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    scent = models.CharField(max_length =150)
    description = models.TextField(max_length=250)
    image = models.TextField(max_length=250)

    def __str__(self):
        return self.chosen_name
 
    def get_absolute_url(self): 
        return reverse('flower-detail', kwargs={'flower_id': self.id})
    
    

