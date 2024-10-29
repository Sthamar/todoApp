from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    
        
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=250,choices= [
        ('completed', 'completed'),
        ('pending', 'pending')
        ], default='pending' )
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    datecompleted = models.DateTimeField( blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.title} of {self.user.username}'