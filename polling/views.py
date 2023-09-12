import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
plt.switch_backend('agg')


import base64
import io
import matplotlib.pyplot as plt

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q, Value, F
from django.db.models.aggregates import Count
from django.db.models import Sum



from django.http import JsonResponse

from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

from rest_framework.mixins import ListModelMixin 

from polling.models import Verification, Election, Candidate
from core.models import UserModel

from feds.models import Citizen

from .serializers import VerificationSerializer,ElectionSerializer, CandidateVotesSerializer

from datetime import date, datetime
# Create your views here.



 


class VerificationViewSet(CreateModelMixin, GenericViewSet):
    queryset = Verification.objects.all()

    serializer_class = VerificationSerializer
    
    
    def create(self, request):    
        
        data = request.data

        # if UserModel.objects.filter(Q(nin=data.get('nin')) & Q(birth_date=birth_date))


        # queryset = Citizen.objects.filter(nin=data.get('nin')).all()
        # for citizen in queryset:
        #     print(citizen.phone)


        # print(queryset)

        try:
            birth_date = data.get('birth_date')

            today = date.today()
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        except ValueError:
            return Response({'Error': 'Date box cannot be empty!'}, status=status.HTTP_400_BAD_REQUEST)

        
        if Citizen.objects.filter(Q(nin=data.get('nin')) & Q(birth_date=birth_date)) and age >= 18:
            queryset = Citizen.objects.filter(nin=data.get('nin'))
            citizen = queryset[0]
            if UserModel.objects.filter(phone=citizen.phone):
                serializer = VerificationSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'Success': 'You are successfully done with your accreditation. You are now eligible to vote'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'Fail': 'You have to registered before using this platform for analysis purposes.'})
        elif Citizen.objects.filter(Q(nin=data.get('nin')) & Q(birth_date=birth_date)) and age < 18:
            return Response({'Fail': 'We have your data in place but your age is not eligible to vote!!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'Fail': "Your NIN cannot be found in the database. Make sure you have registered and your datas are input correctly!!"}, status=status.HTTP_401_UNAUTHORIZED)
    
        

    

class ElectionViewSet(CreateModelMixin, GenericViewSet):
    
    queryset = Election.objects.all()

    def get_serializer_class(self):
        return ElectionSerializer
    

    def create(self, request):
        data = request.data
        # nin = data.get('nin')

    
        if Verification.objects.filter(nin=data.get('voters_nin')):
            serializer = ElectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Success': 'You have successfully casted your vote for your candidate of choice'}, status=status.HTTP_201_CREATED)
        return Response({'error': "You are not eligible to vote!!! Reason: You have not yet done your accreditation!!"}, status=status.HTTP_401_UNAUTHORIZED)


class CountVotesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        votes = Election.objects.values('candidate_id').annotate(count=Count('id'))
        results = {}
        for vote in votes:
            candidate = Candidate.objects.get(id=vote['candidate_id'])
            results[candidate.first_name + ' ' + candidate.last_name] = vote['count']
        candidate_names =  Candidate.objects.all()
        for name in candidate_names:
            if str(name) not in results:
                results[str(name)] = 0

        return Response(results)

        # # displaying the result in a visualised manner e.g histogram
        # candidate_name = []
        # candidate_votes = []
        # for key, value in results.items():
        #     candidate_name.append(key)
        #     candidate_votes.append(value)
        
        #   # Generate a histogram
        # fig, ax = plt.subplots()
        # ax.bar(candidate_name, candidate_votes)
        # ax.set_xlabel('Candidate')
        # ax.set_ylabel('Vote Count')
        # ax.set_title('Candidate Vote Counts')

        # # Convert the histogram image to a base64-encoded string
        # buf = io.BytesIO()
        # fig.savefig(buf, format='png')
        # buf.seek(0)
        # img_data = base64.b64encode(buf.getvalue()).decode('utf-8')
        
        # # Return the histogram image as a JSON response
        # return JsonResponse({'image_data': img_data})


        





