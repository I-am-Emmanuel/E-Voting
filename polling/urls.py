from . import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register('verifications', views.VerificationViewSet)
router.register('voting', views.ElectionViewSet)
# router.register('election-results', views.CandidateVotesViewSet, basename='result')

urlpatterns = [
    path('', include(router.urls)),
    # path('election-results/', views.CandidateVotesViewSet.as_view()),
    path('election-results/', views.CountVotesView().as_view()),
    # path('election-results/', views.CandidateVotesHistogramView.as_view()),
]

