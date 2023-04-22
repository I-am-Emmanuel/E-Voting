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

# class CandidateVotesSerializer(serializers.ModelSerializer):
#     candidate_name = serializers.SerializerMethodField()

#     class Meta:
#         model = CandidateVote
#         fields = ('candidate_name', 'vote_count')

#     def get_candidate_name(self, obj):
#         return f"{obj.candidate.first_name} {obj.candidate.last_name}"

class CandidateVotesSerializer(serializers.Serializer):
    first_name = serializers.CharField(source='candidate.first_name')
    last_name = serializers.CharField(source='candidate.last_name')
    # party_name = serializers.CharField(source='candidate.party_name')
    total_votes = serializers.IntegerField()



