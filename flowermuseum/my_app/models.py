from django.db import models

class Flower(models.Model):
    chosen_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    scent = models.CharField(max_length =150)
    description = models.TextField(max_length=250)
    image = models.TextField(max_length=250)

    def __str__(self):
        return self.chosen_name
 