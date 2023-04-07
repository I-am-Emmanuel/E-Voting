from django.contrib.auth.base_user import BaseUserManager
from feds.models import Citizens

class UserModelManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, phone, password, **extra_data):

        
        if not phone:
            raise ValueError('Phone number is required!')
        
        user = self.model(phone = phone, password=password, **extra_data)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone, password, **extra_data):
        extra_data.setdefault('is_staff', True)
        extra_data.setdefault('is_superuser', True)
        extra_data.setdefault('is_active', True)
    

        return self.create_user(phone, password, **extra_data)