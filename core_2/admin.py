from django.contrib import admin
from . import models
from feds.models import Citizens

# Register your models here.

@admin.register(models.Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ['nin', 'birth_date']


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['states']
    ordering = ['states']
    search_fields = ['states']

@admin.register(models.PresidentialCandidate)
class PresidentialCandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'profile_pics']

# @admin.register(models.SenatorialCandidate)
# class SenatorialCandidateAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'profile_pics']
# # 
# @admin.register(models.HouseOfRepsCandidate)
# class HouseOfRepsCandidateAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'profile_pics']

@admin.register(models.Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ["voters_nin", "voters_state", 'candidate']
    search_fields = ['citizen_details__nin', ]
    autocomplete_fields = ["voters_state"]
    