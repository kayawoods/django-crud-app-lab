from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

AMOUNT = ( 
    ('Cup', '8oz'), 
    ('Pitcher', '32oz'), 
    ('Watering Can', '64oz')
)

class Flower(models.Model):
    chosen_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    scent = models.CharField(max_length =150)
    description = models.TextField(max_length=250)
    image = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chosen_name

    def get_absolute_url(self): 
        return reverse('flower-detail', kwargs={'flower_id': self.id})
    
class Watering(models.Model): 
    date = models.DateField('Watering Date')
    amount = models.CharField(
        max_length=25,
        choices=AMOUNT,
        default=AMOUNT[0][0]
    )                       
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.get_amount_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']