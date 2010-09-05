from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Food(models.Model):
    TYPE_CHOICES=[
        ("MEAT", "meat"), 
        ("FRUIT", "fruit"), 
        ("VEGETABLE", "vegetable")
    ]
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    origin = models.ForeignKey(Location)
    
    @models.permalink
    def get_absolute_url(self):
        return ('food_view', [self.id])
        
    def __str__(self):
        return "Food[id=%s, name=%s, type=%s, origin=%s]"%(self.id, self.name, self.type, self.origin)