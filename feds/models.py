from django.db import models
from  django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Citizen(models.Model):
    nin = models.CharField(max_length=11, unique=True, validators = [MinLengthValidator(11, message='Your NIN should be 11 digit numbers') ,MaxLengthValidator(11)] )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=False)
    phone = models.CharField(max_length=14, blank=False, unique=True)
    email = models.EmailField(null=True, blank=True)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')



    
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
