from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class tweet(models.Model):
    text = models.TextField(max_length= 200, default= '')
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE) 
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.user.userame}'
    
