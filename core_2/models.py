from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from feds.models import Citizens


# Create your models here.


class Verification(models.Model):
    nin = models.CharField(max_length=11, unique=True, validators = [MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), MaxLengthValidator(11)] )
    birth_date = models.DateField(null=False)
    
    def __str__(self) -> str:
        return self.nin

class State(models.Model):
    states = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.states

class PresidentialCandidate(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        ordering = ['first_name']

# class SenatorialCandidate(models.Model):
#     first_name = models.CharField(max_length=50, blank=False)
#     last_name = models.CharField(max_length=50, blank=True)
#     profile_pics = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')


# class HouseOfRepsCandidate(models.Model):
#     first_name = models.CharField(max_length=50, blank=False)
#     last_name = models.CharField(max_length=50, blank=True)
#     profile_pics = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')
    


class Election(models.Model):
    voters_nin = models.CharField(max_length=11, validators = [MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), MaxLengthValidator(11)], unique=True)
    voters_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=False)
    candidate = models.ForeignKey(PresidentialCandidate, on_delete=models.CASCADE)

# class ResultTable(models.Model):
#     accredited_voters = models.ForeignKey(Verification, on_delete=models.CASCADE)
    
    # vote_count = pass

    
    
    