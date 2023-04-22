from . import views
from django.urls import path, include
from django.views.generic import TemplateView
# from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html')),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    # path('verify/otp', views.VerifyOTP.as_view()),
]

