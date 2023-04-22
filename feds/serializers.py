from . models import Citizen
from rest_framework import serializers

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ['nin', 'first_name', 'last_name', 'birth_date', 'phone', 'email', 'profile_pics']
        ordering = ['first_name']
    # citizen_contact_detail = serializers.SerializerMethodField(method_name='field_id')

    # def field_id(self, query:Citizens):
    #     if query.phone_number is not None and query.email_field is not None:
    #         return query.email_field
    #     elif query.phone_number is None and query.email_field is not None:
    #         return query.email_field
    #     return query.phone_number



