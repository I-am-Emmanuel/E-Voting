from . import views
from django.urls import path, include
# from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('verify/otp', views.VerifyOTP.as_view()),
]

