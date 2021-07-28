from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

class Post(models.Model):
    message = models.CharField(max_length=1000)
    photo = CloudinaryField('image',default='Image')
    date=models.DateTimeField(auto_now_add=True)
    pollution_type = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    estimate_choices = [
        (0,"0"),
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10")
        ]
    estimate=models.CharField(max_length=10,choices=estimate_choices,default=0)
    
    def __str__(self):
        return self.pollution_type

class Cleanup(models.Model):
    location = models.CharField(max_length=50)
    organizer = models.CharField(max_length=30)
    organizer_contact= models.CharField(max_length=12)
    date=models.DateTimeField(auto_now_add=True)
    paybill = models.CharField(max_length=7)
    amount = models.CharField(max_length=10)
    
    def __str__(self):
        return self.organizer

class Response(models.Model):
    reaction= models.TextField(max_length=1000)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    clean_id=models.ForeignKey(Cleanup, on_delete=models.CASCADE)
    estimate=models.CharField(max_length=3)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reaction

class Reactions(models.Model):
    reaction= models.TextField(max_length=1000)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    clean_id=models.ForeignKey(Cleanup, on_delete=models.CASCADE)
    estimate=models.CharField(max_length=3)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reaction