from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Citizen)
class CitizensAdmin(admin.ModelAdmin):
    list_display = ['nin', 'first_name', 'last_name', 'contact_details', 'profile_pics', 'birth_date']
    search_fields = ['nin']
    list_per_page = 15
    ordering = ['first_name']
    list_filter = ['nin']


    def contact_details(self, query: models.Citizen):
        if query.phone is not None and query.email is not None:
            return query.email
        return query.phone
    
    
    





