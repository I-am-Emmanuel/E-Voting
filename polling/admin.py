from django.contrib import admin
from . import models
from feds.models import Citizen

# Register your models here.

@admin.register(models.Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ['nin', 'birth_date']


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['states']
    ordering = ['states']
    search_fields = ['states']

@admin.register(models.Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'profile_pics']



@admin.register(models.Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ["voters_nin", "voters_state", 'candidate']
    search_fields = ['citizen_details__nin', ]
    autocomplete_fields = ["voters_state"]

# @admin.register(models.CandidateVote)
# class CandidateVoteAdmin(admin.ModelAdmin):
#     list_display = ['candidate__first_name', 'candidate__last_name']

# @admin.register(models.Co)
# class CountVoteAdmin(admin.ModelAdmin):
#     list_display = ['candidate__first_name', 'candidate__last_name']