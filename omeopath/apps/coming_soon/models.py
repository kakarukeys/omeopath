from django.db import models

# Create your models here.

class Prospect(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name="name")
    email = models.EmailField(unique=True, verbose_name="email address")
    
    class Meta:
        verbose_name = "Notification sign-up"
        
