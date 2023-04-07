from . import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register('verifications', views.VerificationViewSet)
router.register('voting', views.ElectionViewSet)
router.register('results', views.ElectionResultViewSet, basename='results')

urlpatterns = [
    path('', include(router.urls))
]

# router = routers.DefaultRouter()
# router.register('verifications', views.VerificationViewSet)
# router.register('voting', views.ElectionViewSet)



# verifications_router = routers.NestedDefaultRouter(router, 'verifications', lookup='verification')
# verifications_router.register('election', views.ElectionViewSet, basename='citizen-vote' )

# urlpatterns = [ 
# path('', include(router.urls + verifications_router.urls))
# ]