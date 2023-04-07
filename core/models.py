from django.db import models
from  django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser
import uuid
from . manager import UserModelManager
# Create your models here.

class UserModel(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14, unique=True, blank=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True)
    username=None
    email = None
    password = models.CharField(max_length=250, validators = [MinLengthValidator(7, message='Your password is too short! Minimum of 8 length is required')])
    
    def __str__(self):
        return self.phone

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserModelManager()



    # password = models.CharField(max_length=250)
    # otp_enabled = models.BooleanField(default=False)
    # otp_verified = models.BooleanField(default=False)
    # otp_base32 = models.CharField(max_length=255, null=True)
    # otp_auth_url = models.CharField(max_length=255, null=True)
    # username = models.CharField(max_length=32, unique=True)
    
    # email = None


    # USERNAME_FIELD = 'phone'
    # EMAIL_FIELD = 'phone'
    