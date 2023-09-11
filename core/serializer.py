from rest_framework import serializers
from core.models import UserModel
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .sender import send_otp_to_phone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['phone', 'password']
                
        extra_kwargs = {
            'password': {'write_only': True}
        }
       

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.phone = instance.phone
        # instance.otp = send_otp_to_phone(phone=instance.phone)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# class VerifyOTPSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ['phone', 'otp']
        

    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


# class UserGenerateOTPSerializer(serializers.ModelSerializer):
#     user_id = serializers.CharField(max_length=50)
#     class Meta:
#         model = UserModel
#         fields = ['id','phone', 'user_id']

#     # MYLO4I7BSKCVMPTPLLUNNTYH4ARAVXTL


# class VerifyOTPSerializer(serializers.ModelSerializer):
#     user_id = serializers.CharField(max_length=50)
#     token = serializers.CharField(max_length=6, validators = [MinLengthValidator(6, message='Your OTP should be 6 digit numbers'), MaxLengthValidator(6)])
#     class Meta:
#         model = UserModel
#         fields = ['id', 'user_id', 'token']




        

