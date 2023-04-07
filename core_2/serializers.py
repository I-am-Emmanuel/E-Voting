from . models import Verification, Election
from rest_framework import serializers
from django.contrib.auth import authenticate


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ['nin', 'birth_date']


class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ["voters_nin", "voters_state", 'candidate']

class ElectionResultSerializer(serializers.ModelSerializer):
    class Meta:
        pass


