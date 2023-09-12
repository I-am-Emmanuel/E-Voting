from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core import validators
from feds.models import Citizen
from django.core.exceptions import ValidationError


# Create your models here.


class Verification(models.Model):
    nin = models.CharField(max_length=11, unique=True, validators = [MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), MaxLengthValidator(11)] )
    birth_date = models.DateField(null=False)
    
    def __str__(self) -> str:
        return self.nin

class State(models.Model):
    states = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self) -> str:
        return self.states

class Candidate(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    profile_pics = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')

    def __str__(self) -> str:
        return self.last_name
    
    class Meta:
        ordering = ['first_name']

def check_for_state_alphabet(value:State):
    if not value.states.isalpha():
        raise ValidationError('You can\'t use this field. Make sure you have select the right field!')

def check_for_candidate_alphabet(value:Candidate):
    if not value.last_name.isalpha():
        raise ValidationError('You can\'t use this field. Make sure you have select the right field!')
    

class Election(models.Model):
    voters_nin = models.CharField(max_length=11, validators = [MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), MaxLengthValidator(11)], unique=True)
    voters_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=False, validators=[check_for_state_alphabet])
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=False, validators=[check_for_candidate_alphabet])




    
    
    