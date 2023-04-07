from . import views
from django.urls import path

urlpatterns = [
    # path('', views.greetings),
    # path('citizen/', views.citizen_list),
    path('citizen/', views.CitizensList.as_view()),
    # path('citizen/<int:id>/', views.citizen_details),
    path('citizen/<int:id>/', views.CitizensDetails.as_view()),
]