from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Q, Value, F
# from rest_framework.views 
from rest_framework.mixins import CreateModelMixin

from django.contrib.auth import authenticate
from core.serializer import UserSerializer, UserLoginSerializer
# from core.serializer import UserSerializer, VerifyOTPSerializer, UserLoginSerializer
from core.models import UserModel
from .sender import send_otp_to_phone
# import pyotp
from feds.models import Citizen
from electronic_voting import settings
from rest_framework.decorators import api_view

# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def post(self, request):
        data = request.data
        mobilePhone = data.get('phone')

        if UserModel.objects.filter(phone=mobilePhone).exists():
            return Response({'status': 'fail', 'message': 'Mobile number has already been registered before now!'}, status=status.HTTP_400_BAD_REQUEST)

        if Citizen.objects.filter(phone=mobilePhone):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)    
            serializer.save()
        
            return Response({"status": "success", 'message': "Your registration is successfully done"}, status=status.HTTP_200_OK)
            # return Response({"status": "success", 'message': f"Otp Successfully sent to {mobilePhone}"}, status=status.HTTP_200_OK)
        return Response({'status': 'fail', 'message': 'Your number is not associated with any NIN'}, status=status.HTTP_400_BAD_REQUEST)



class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    queryset = UserModel.objects.all()

    def post(self, request):
        data = request.data
        phone = data.get('phone')
        password= data.get('password') 
        
        

        user = authenticate(phone=phone, password=password)

        if user is None:
            return Response({"status": "Fail", "message": "This field need a correct data!! Make sure you input your registered data correctly!!!"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'status': 'Fail', 'message': 'Incorrect details!!'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(user)
    
        return Response({"status": 'Login successful', 'user': serializer.data })
    

    

# class VerifyOTP(generics.GenericAPIView):
#     serializer_class = VerifyOTPSerializer
#     queryset = UserModel.objects.all()

#     def post(self, request):
#         message = "Token is invalid!"
#         data = request.data
        
#         if data.get('phone') is None:
#             return Response({"status": "fail", "message": "Phone is required!!"}, status=status.HTTP_404_NOT_FOUND)

#         if data.get('otp') is None:
#              return Response({"status": "fail", "message": "Otp is required!!"}, status=status.HTTP_404_NOT_FOUND)
#         try:
        
#             userobj = UserModel.objects.get(phone=data.get('phone'))

#         except Exception as e:
#             return Response({'status': 'error', 'message': 'Phone number is invalid!'}, status=status.HTTP_404_NOT_FOUND)
            
          
#         if userobj.otp == data.get('otp'):
#             userobj.is_phone_verified = True
#             userobj.save()
#             return Response({'status': 'success', 'message': 'Otp verified'}, status=status.HTTP_200_OK)
#         return Response({"status": "fail", "message": message}, status=status.HTTP_400_BAD_REQUEST)
            
    
       
        
